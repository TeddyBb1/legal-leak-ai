import React, { useState } from "react";
import ResultCard from "./components/ResultCard";

function App() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setResults(data.results);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <h1 className="text-3xl font-bold mb-6">LegalLeak AI</h1>
      <div className="bg-gray-800 p-6 rounded-xl shadow-md">
        <input
          type="file"
          accept=".pdf,.docx,.txt"
          onChange={handleFileChange}
          className="mb-4"
        />
        <button
          onClick={handleUpload}
          disabled={loading}
          className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded text-white"
        >
          {loading ? "Analizăm..." : "Încarcă și analizează"}
        </button>
      </div>

      {results.length > 0 && (
        <div className="mt-8">
          <h2 className="text-2xl mb-4">Probleme identificate:</h2>
          <div className="space-y-4">
            {results.map((res, index) => (
              <ResultCard key={index} data={res} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
