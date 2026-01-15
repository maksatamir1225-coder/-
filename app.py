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
    'ag-hcl': { precipitate: 'AgCl', color: '#f0f0f0', colorName: 'Белый', description: 'Белый творожистый осадок', equation: 'Ag⁺ + Cl⁻ → AgCl↓', group: 'I' },
    'pb-hcl': { precipitate: 'PbCl₂', color: '#fafafa', colorName: 'Белый', description: 'Белый кристаллический осадок', equation: 'Pb²⁺ + 2Cl⁻ → PbCl₂↓', group: 'I' },
    'hg2-hcl': { precipitate: 'Hg₂Cl₂', color: '#f5f5f5', colorName: 'Белый', description: 'Белый осадок (каломель)', equation: 'Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓', group: 'I' },
    'cu-h2s': { precipitate: 'CuS', color: '#1a1a1a', colorName: 'Черный', description: 'Черный осадок', equation: 'Cu²⁺ + H₂S → CuS↓ + 2H⁺', group: 'II' },
    'cu-naoh': { precipitate: 'Cu(OH)₂', color: '#4da6ff', colorName: 'Голубой', description: 'Голубой желатинообразный осадок', equation: 'Cu²⁺ + 2OH⁻ → Cu(OH)₂↓', group: 'II' },
    'fe2-naoh': { precipitate: 'Fe(OH)₂', color: '#d0e8d0', colorName: 'Зеленовато-белый', description: 'Зеленовато-белый осадок', equation: 'Fe²⁺ + 2OH⁻ → Fe(OH)₂↓', group: 'II' },
    'fe3-naoh': { precipitate: 'Fe(OH)₃', color: '#cc7733', colorName: 'Бурый', description: 'Бурый осадок', equation: 'Fe³⁺ + 3OH⁻ → Fe(OH)₃↓', group: 'II' },
    'fe3-kcns': { precipitate: 'Fe(CNS)₃', color: '#dd0000', colorName: 'Кроваво-красный', description: 'Кроваво-красное окрашивание', equation: 'Fe³⁺ + 3CNS⁻ → Fe(CNS)₃', group: 'II', solution: true },
    'fe2-k3fecn6': { precipitate: 'Fe₃[Fe(CN)₆]₂', color: '#1a4d7a', colorName: 'Темно-синий', description: 'Турнбулева синь', equation: 'Fe²⁺ + K₃[Fe(CN)₆] → Fe₃[Fe(CN)₆]₂↓', group: 'II' },
    'fe3-k4fecn6': { precipitate: 'Fe₄[Fe(CN)₆]₃', color: '#004080', colorName: 'Берлинская лазурь', description: 'Синий осадок', equation: 'Fe³⁺ + K₄[Fe(CN)₆] → Fe₄[Fe(CN)₆]₃↓', group: 'II' },
    'al-naoh': { precipitate: 'Al(OH)₃', color: '#f8f8f8', colorName: 'Белый', description: 'Белый желатинообразный осадок', equation: 'Al³⁺ + 3OH⁻ → Al(OH)₃↓', group: 'III' },
    'zn-naoh': { precipitate: 'Zn(OH)₂', color: '#ffffff', colorName: 'Белый', description: 'Белый осадок', equation: 'Zn²⁺ + 2OH⁻ → Zn(OH)₂↓', group: 'III' },
    'zn-h2s': { precipitate: 'ZnS', color: '#fafafa', colorName: 'Белый', description: 'Белый осадок', equation: 'Zn²⁺ + H₂S → ZnS↓ + 2H⁺', group: 'III' },
    'ba-na2so4': { precipitate: 'BaSO₄', color: '#f5f5f5', colorName: 'Белый', description: 'Белый кристаллический осадок', equation: 'Ba²⁺ + SO₄²⁻ → BaSO₄↓', group: 'IV' },
    'ca-na2so4': { precipitate: 'CaSO₄', color: '#fafafa', colorName: 'Белый', description: 'Белый осадок', equation: 'Ca²⁺ + SO₄²⁻ → CaSO₄↓', group: 'IV' }
  };

  const performReaction = () => {
    if (!selectedCation || !selectedReagent) return;
    setIsAnimating(true);
    const reactionKey = `${selectedCation}-${selectedReagent}`;
    const result = reactions[reactionKey];
    setTimeout(() => {
      setReactionResult(result || { precipitate: 'Нет реакции', color: 'transparent', colorName: 'Нет изменений', description: 'Осадок не образуется', equation: 'Реакция не происходит' });
      setIsAnimating(false);
    }, 1500);
  };

  const reset = () => {
    setSelectedCation(null);
    setSelectedReagent(null);
    setReactionResult(null);
    setIsAnimating(false);
  };

  const getCationColor = () => cations.find(c => c.id === selectedCation)?.color || '#e8f4f8';

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-pink-50 to-blue-50 p-8">{/* UI omitted for brevity in README; full UI identical to your version */}</div>
  );
};

export default CationLab;
