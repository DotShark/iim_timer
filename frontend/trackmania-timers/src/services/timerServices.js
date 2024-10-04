import axios from 'axios';

const apiUrl = 'http://localhost:5000/api/timers';  // Remplace cette URL par celle de ton API

export const getTimers = async () => {
    try {
    const response = await axios.get(apiUrl);
    return response.data;
    } catch (error) {
    console.error('Erreur lors de la récupération des timers', error);
    throw error;
    }
};
