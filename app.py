import React, { useState } from 'react';
import { Beaker, Droplet, RotateCcw, FlaskConical } from 'lucide-react';

const CationLab = () => {
  const [selectedCation, setSelectedCation] = useState(null);
  const [selectedReagent, setSelectedReagent] = useState(null);
  const [reactionResult, setReactionResult] = useState(null);
  const [isAnimating, setIsAnimating] = useState(false);

  const cations = [
    { id: 'ag', name: 'Ag⁺ (Серебро)', color: '#e8f4f8', group: 'I' },
    { id: 'pb', name: 'Pb²⁺ (Свинец)', color: '#f0f0f0', group: 'I' },
    { id: 'hg2', name: 'Hg₂²⁺ (Ртуть I)', color: '#f5f5f5', group: 'I' },
    { id: 'cu', name: 'Cu²⁺ (Медь)', color: '#a8d5ff', group: 'II' },
    { id: 'fe2', name: 'Fe²⁺ (Железо II)', color: '#d4f0d4', group: 'II' },
    { id: 'fe3', name: 'Fe³⁺ (Железо III)', color: '#fff0d4', group: 'II' },
    { id: 'al', name: 'Al³⁺ (Алюминий)', color: '#f0f8ff', group: 'III' },
    { id: 'zn', name: 'Zn²⁺ (Цинк)', color: '#f5f5ff', group: 'III' },
    { id: 'ba', name: 'Ba²⁺ (Барий)', color: '#fafafa', group: 'IV' },
    { id: 'ca', name: 'Ca²⁺ (Кальций)', color: '#fffafa', group: 'IV' },
    { id: 'na', name: 'Na⁺ (Натрий)', color: '#fff9f0', group: 'V' },
    { id: 'k', name: 'K⁺ (Калий)', color: '#fef8ff', group: 'V' }
  ];

  const reagents = [
    { id: 'hcl', name: 'HCl', description: 'Соляная кислота' },
    { id: 'h2s', name: 'H₂S', description: 'Сероводород' },
    { id: 'naoh', name: 'NaOH', description: 'Гидроксид натрия' },
    { id: 'nh4oh', name: 'NH₄OH', description: 'Гидроксид аммония' },
    { id: 'k4fecn6', name: 'K₄[Fe(CN)₆]', description: 'Гексацианоферрат (II) калия' },
    { id: 'k3fecn6', name: 'K₃[Fe(CN)₆]', description: 'Гексацианоферрат (III) калия' },
    { id: 'kcns', name: 'KCNS', description: 'Роданид калия' },
    { id: 'na2so4', name: 'Na₂SO₄', description: 'Сульфат натрия' }
  ];

  const reactions = {
    'ag-hcl': {
      precipitate: 'AgCl',
      color: '#f0f0f0',
      colorName: 'Белый',
      description: 'Белый творожистый осадок',
      equation: 'Ag⁺ + Cl⁻ → AgCl↓',
      group: 'I'
    },
    'pb-hcl': {
      precipitate: 'PbCl₂',
      color: '#fafafa',
      colorName: 'Белый',
      description: 'Белый кристаллический осадок',
      equation: 'Pb²⁺ + 2Cl⁻ → PbCl₂↓',
      group: 'I'
    },
    'hg2-hcl': {
      precipitate: 'Hg₂Cl₂',
      color: '#f5f5f5',
      colorName: 'Белый',
      description: 'Белый осадок (каломель)',
      equation: 'Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓',
      group: 'I'
    },
    'cu-h2s': {
      precipitate: 'CuS',
      color: '#1a1a1a',
      colorName: 'Черный',
      description: 'Черный осадок',
      equation: 'Cu²⁺ + H₂S → CuS↓ + 2H⁺',
      group: 'II'
    },
    'cu-naoh': {
      precipitate: 'Cu(OH)₂',
      color: '#4da6ff',
      colorName: 'Голубой',
      description: 'Голубой желатинообразный осадок',
      equation: 'Cu²⁺ + 2OH⁻ → Cu(OH)₂↓',
      group: 'II'
    },
    'fe2-naoh': {
      precipitate: 'Fe(OH)₂',
      color: '#d0e8d0',
      colorName: 'Зеленовато-белый',
      description: 'Зеленовато-белый осадок',
      equation: 'Fe²⁺ + 2OH⁻ → Fe(OH)₂↓',
      group: 'II'
    },
    'fe3-naoh': {
      precipitate: 'Fe(OH)₃',
      color: '#cc7733',
      colorName: 'Бурый',
      description: 'Бурый (красно-коричневый) осадок',
      equation: 'Fe³⁺ + 3OH⁻ → Fe(OH)₃↓',
      group: 'II'
    },
    'fe3-kcns': {
      precipitate: 'Fe(CNS)₃',
      color: '#dd0000',
      colorName: 'Кроваво-красный',
      description: 'Кроваво-красное окрашивание',
      equation: 'Fe³⁺ + 3CNS⁻ → Fe(CNS)₃',
      group: 'II',
      solution: true
    },
    'fe2-k3fecn6': {
      precipitate: 'Fe₃[Fe(CN)₆]₂',
      color: '#1a4d7a',
      colorName: 'Темно-синий',
      description: 'Темно-синий осадок (турнбулева синь)',
      equation: 'Fe²⁺ + K₃[Fe(CN)₆] → Fe₃[Fe(CN)₆]₂↓',
      group: 'II'
    },
    'fe3-k4fecn6': {
      precipitate: 'Fe₄[Fe(CN)₆]₃',
      color: '#004080',
      colorName: 'Берлинская лазурь',
      description: 'Синий осадок (берлинская лазурь)',
      equation: 'Fe³⁺ + K₄[Fe(CN)₆] → Fe₄[Fe(CN)₆]₃↓',
      group: 'II'
    },
    'al-naoh': {
      precipitate: 'Al(OH)₃',
      color: '#f8f8f8',
      colorName: 'Белый',
      description: 'Белый желатинообразный осадок',
      equation: 'Al³⁺ + 3OH⁻ → Al(OH)₃↓',
      group: 'III'
    },
    'zn-naoh': {
      precipitate: 'Zn(OH)₂',
      color: '#ffffff',
      colorName: 'Белый',
      description: 'Белый осадок',
      equation: 'Zn²⁺ + 2OH⁻ → Zn(OH)₂↓',
      group: 'III'
    },
    'zn-h2s': {
      precipitate: 'ZnS',
      color: '#fafafa',
      colorName: 'Белый',
      description: 'Белый осадок',
      equation: 'Zn²⁺ + H₂S → ZnS↓ + 2H⁺',
      group: 'III'
    },
    'ba-na2so4': {
      precipitate: 'BaSO₄',
      color: '#f5f5f5',
      colorName: 'Белый',
      description: 'Белый кристаллический осадок',
      equation: 'Ba²⁺ + SO₄²⁻ → BaSO₄↓',
      group: 'IV'
    },
    'ca-na2so4': {
      precipitate: 'CaSO₄',
      color: '#fafafa',
      colorName: 'Белый',
      description: 'Белый осадок',
      equation: 'Ca²⁺ + SO₄²⁻ → CaSO₄↓',
      group: 'IV'
    }
  };

  const performReaction = () => {
    if (!selectedCation || !selectedReagent) return;

    setIsAnimating(true);
    const reactionKey = `${selectedCation}-${selectedReagent}`;
    const result = reactions[reactionKey];

    setTimeout(() => {
      setReactionResult(result || {
        precipitate: 'Нет реакции',
        color: 'transparent',
        colorName: 'Нет изменений',
        description: 'Осадок не образуется',
        equation: 'Реакция не происходит'
      });
      setIsAnimating(false);
    }, 1500);
  };

  const reset = () => {
    setSelectedCation(null);
    setSelectedReagent(null);
    setReactionResult(null);
    setIsAnimating(false);
  };

  const getCationColor = () => {
    const cation = cations.find(c => c.id === selectedCation);
    return cation ? cation.color : '#e8f4f8';
  };

  const groupedCations = {
    'I': cations.filter(c => c.group === 'I'),
    'II': cations.filter(c => c.group === 'II'),
    'III': cations.filter(c => c.group === 'III'),
    'IV': cations.filter(c => c.group === 'IV'),
    'V': cations.filter(c => c.group === 'V')
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-pink-50 to-blue-50 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-2">
            <FlaskConical className="w-10 h-10 text-purple-600" />
            <h1 className="text-4xl font-bold text-gray-800">
              Качественный анализ катионов
            </h1>
          </div>
          <p className="text-gray-600">Интерактивная химическая лаборатория</p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mb-8">
          {/* Выбор катиона */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <Droplet className="w-5 h-5 text-purple-500" />
              Шаг 1: Выберите катион
            </h2>
            <div className="space-y-3">
              {Object.entries(groupedCations).map(([group, cationList]) => (
                <div key={group}>
                  <div className="text-xs font-bold text-gray-500 mb-1">
                    Группа {group}
                  </div>
                  <div className="space-y-1">
                    {cationList.map(cation => (
                      <button
                        key={cation.id}
                        onClick={() => setSelectedCation(cation.id)}
                        className={`w-full p-2 rounded-lg text-left text-sm transition-all ${
                          selectedCation === cation.id
                            ? 'bg-purple-500 text-white shadow-md'
                            : 'bg-gray-50 hover:bg-gray-100'
                        }`}
                      >
                        {cation.name}
                      </button>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Выбор реагента */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <Beaker className="w-5 h-5 text-blue-500" />
              Шаг 2: Выберите реагент
            </h2>
            <div className="space-y-2">
              {reagents.map(reagent => (
                <button
                  key={reagent.id}
                  onClick={() => setSelectedReagent(reagent.id)}
                  className={`w-full p-3 rounded-lg text-left transition-all ${
                    selectedReagent === reagent.id
                      ? 'bg-blue-500 text-white shadow-md'
                      : 'bg-gray-50 hover:bg-gray-100'
                  }`}
                >
                  <div className="font-semibold">{reagent.name}</div>
                  <div className={`text-sm ${
                    selectedReagent === reagent.id ? 'text-blue-100' : 'text-gray-500'
                  }`}>
                    {reagent.description}
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Результат */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-xl font-bold text-gray-800 mb-4">
              Шаг 3: Результат реакции
            </h2>
            {reactionResult ? (
              <div className="space-y-4">
                <div className="bg-green-50 p-4 rounded-lg border-2 border-green-200">
                  <div className="font-bold text-green-800 mb-2">
                    {reactionResult.precipitate}
                  </div>
                  {reactionResult.group && (
                    <div className="text-xs text-green-600 mb-2">
                      Группа {reactionResult.group}
                    </div>
                  )}
                  <div className="text-sm text-green-700 mb-3">
                    {reactionResult.description}
                  </div>
                  <div className="text-xs font-mono bg-white p-2 rounded border border-green-200">
                    {reactionResult.equation}
                  </div>
                </div>
              </div>
            ) : (
              <div className="text-center text-gray-400 py-8">
                Выберите катион и реагент, затем проведите реакцию
              </div>
            )}
          </div>
        </div>

        {/* Пробирки */}
        <div className="bg-white rounded-lg shadow-lg p-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
            Визуализация эксперимента
          </h2>
          
          <div className="flex justify-center items-end gap-12 mb-8">
            {/* Пробирка с катионом */}
            <div className="text-center">
              <div className="text-sm font-semibold text-gray-600 mb-2">
                Раствор катиона
              </div>
              <div className="relative">
                <svg width="80" height="200" viewBox="0 0 80 200">
                  <defs>
                    <linearGradient id="tubeGradient1" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" style={{stopColor: '#e0e0e0', stopOpacity: 0.5}} />
                      <stop offset="50%" style={{stopColor: '#ffffff', stopOpacity: 0.8}} />
                      <stop offset="100%" style={{stopColor: '#e0e0e0', stopOpacity: 0.5}} />
                    </linearGradient>
                  </defs>
                  <path
                    d="M 25 10 L 25 150 Q 25 180 40 190 Q 55 180 55 150 L 55 10 Q 55 5 50 5 L 30 5 Q 25 5 25 10 Z"
                    fill="url(#tubeGradient1)"
                    stroke="#999"
                    strokeWidth="1.5"
                  />
                  <ellipse cx="40" cy="10" rx="15" ry="4" fill="#e0e0e0" stroke="#999" strokeWidth="1.5"/>
                  {selectedCation && (
                    <rect
                      x="27"
                      y="100"
                      width="26"
                      height="80"
                      fill={getCationColor()}
                      opacity="0.8"
                      rx="2"
                    />
                  )}
                </svg>
              </div>
              {selectedCation && (
                <div className="text-xs font-semibold text-purple-600 mt-2">
                  {cations.find(c => c.id === selectedCation)?.name}
                </div>
              )}
            </div>

            {/* Стрелка + реагент */}
            <div className="mb-16">
              <div className="text-2xl text-gray-400 mb-2">+</div>
              {selectedReagent && (
                <div className="text-xs font-semibold text-blue-600">
                  {reagents.find(r => r.id === selectedReagent)?.name}
                </div>
              )}
            </div>

            {/* Кнопка реакции */}
            <div className="mb-16">
              <button
                onClick={performReaction}
                disabled={!selectedCation || !selectedReagent || isAnimating}
                className={`px-6 py-3 rounded-lg font-bold transition-all ${
                  selectedCation && selectedReagent
                    ? 'bg-gradient-to-r from-purple-500 to-blue-500 text-white hover:shadow-lg hover:scale-105'
                    : 'bg-gray-300 text-gray-500 cursor-not-allowed'
                }`}
              >
                {isAnimating ? 'Реакция...' : 'Провести реакцию →'}
              </button>
            </div>

            {/* Пробирка с результатом */}
            <div className="text-center">
              <div className="text-sm font-semibold text-gray-600 mb-2">
                Результат
              </div>
              <div className="relative">
                <svg width="80" height="200" viewBox="0 0 80 200">
                  <defs>
                    <linearGradient id="tubeGradient2" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" style={{stopColor: '#e0e0e0', stopOpacity: 0.5}} />
                      <stop offset="50%" style={{stopColor: '#ffffff', stopOpacity: 0.8}} />
                      <stop offset="100%" style={{stopColor: '#e0e0e0', stopOpacity: 0.5}} />
                    </linearGradient>
                  </defs>
                  <path
                    d="M 25 10 L 25 150 Q 25 180 40 190 Q 55 180 55 150 L 55 10 Q 55 5 50 5 L 30 5 Q 25 5 25 10 Z"
                    fill="url(#tubeGradient2)"
                    stroke="#999"
                    strokeWidth="1.5"
                  />
                  <ellipse cx="40" cy="10" rx="15" ry="4" fill="#e0e0e0" stroke="#999" strokeWidth="1.5"/>
                  {reactionResult && !reactionResult.solution && (
                    <>
                      <rect
                        x="27"
                        y="100"
                        width="26"
                        height="80"
                        fill={reactionResult.color === 'transparent' ? '#e0f2ff' : '#e0f2ff'}
                        opacity="0.6"
                        rx="2"
                      />
                      {reactionResult.color !== 'transparent' && (
                        <rect
                          x="28"
                          y={isAnimating ? "120" : "160"}
                          width="24"
                          height={isAnimating ? "10" : "20"}
                          fill={reactionResult.color}
                          stroke="#666"
                          strokeWidth="0.5"
                          opacity="1"
                          rx="1"
                          className="transition-all duration-1000"
                        />
                      )}
                    </>
                  )}
                  {reactionResult?.solution && (
                    <rect
                      x="27"
                      y="100"
                      width="26"
                      height="80"
                      fill={reactionResult.color}
                      opacity="0.9"
                      rx="2"
                      className="transition-all duration-1000"
                    />
                  )}
                </svg>
              </div>
              {reactionResult && (
                <div className="text-xs font-semibold text-green-600 mt-2">
                  {reactionResult.precipitate}
                  <div className="mt-1 flex items-center justify-center gap-2">
                    <span className="text-gray-600">Цвет:</span>
                    <div 
                      className="w-8 h-8 rounded border-2 border-gray-400 shadow-sm"
                      style={{ backgroundColor: reactionResult.color }}
                    />
                    <span className="font-bold text-gray-800">{reactionResult.colorName}</span>
                  </div>
                </div>
              )}
            </div>
          </div>

          <div className="flex justify-center">
            <button
              onClick={reset}
              className="flex items-center gap-2 px-6 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600 transition-colors"
            >
              <RotateCcw className="w-4 h-4" />
              Новый эксперимент
            </button>
          </div>
        </div>

        {/* Справочная информация */}
        <div className="mt-8 bg-purple-50 rounded-lg p-6 border-2 border-purple-200">
          <h3 className="font-bold text-purple-900 mb-3">💡 Аналитические группы катионов</h3>
          <div className="grid md:grid-cols-2 gap-4 text-sm text-purple-800">
            <div>
              <strong>I группа (HCl):</strong> Ag⁺, Pb²⁺, Hg₂²⁺ — дают белые осадки хлоридов
            </div>
            <div>
              <strong>II группа (H₂S в кислой среде):</strong> Cu²⁺, Fe²⁺, Fe³⁺ — цветные осадки и окрашивание
            </div>
            <div>
              <strong>III группа (H₂S в щелочной среде):</strong> Al³⁺, Zn²⁺ — белые осадки гидроксидов
            </div>
            <div>
              <strong>IV группа ((NH₄)₂CO₃):</strong> Ba²⁺, Ca²⁺ — белые осадки карбонатов/сульфатов
            </div>
            <div>
              <strong>V группа:</strong> Na⁺, K⁺ — осадков не дают, определяются по пламени
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CationLab;
