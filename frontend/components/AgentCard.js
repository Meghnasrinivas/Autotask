import React from 'react';
import { motion } from 'framer-motion';

export default function AgentCard({ agent, selected, onToggle }) {
  return (
    <motion.button
      onClick={onToggle}
      whileHover={{ scale: 1.03 }}
      whileTap={{ scale: 0.98 }}
      className={`agent-card ${selected ? 'selected' : ''}`}
    >
      <h3>{agent.name}</h3>
      <p>{agent.role}</p>
      <span>{selected ? 'Selected' : 'Tap to select'}</span>
    </motion.button>
  );
}
