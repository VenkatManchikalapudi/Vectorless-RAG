import { render, screen } from '@testing-library/react';
import App from './App';
import '@testing-library/jest-dom';

describe('App', () => {
  it('renders PDF Summary App title', () => {
    render(<App />);
    expect(screen.getByText(/PDF Summary App/i)).toBeInTheDocument();
  });
});
