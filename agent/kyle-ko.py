class MyAgent(BaseAgent):
    def step(self, obs, reward):
        return (self.col_offset + random.randint(0, self.cols_n-1) * self.block_len, self.row_offset + random.randint(0, self.rows_n-1) * self.block_len), pygame.USEREVENT
