import React from "react";

function ResultCard({ data }) {
  return (
    <div className="bg-gray-800 p-4 rounded-lg shadow">
      <p className="text-sm text-gray-400 mb-1">🧠 Tip: <strong>{data.type}</strong></p>
      <p className="mb-2"><span className="font-semibold">📌 Text:</span> {data.text}</p>
      <p className="text-green-400"><strong>💡 Explicație:</strong> {data.explanation}</p>
    </div>
  );
}

export default ResultCard;
