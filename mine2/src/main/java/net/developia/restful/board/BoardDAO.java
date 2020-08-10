package net.developia.restful.board;

import java.sql.SQLException;
import java.util.List;

public interface BoardDAO {

	List<BoardDTO> getBoardList() throws Exception;

	void insertBoard(BoardDTO boardDTO) throws Exception;

	void insertArticle(ArticleDTO articleDTO) throws Exception;

	BoardDTO getBoard(int boa_no) throws Exception;

	List<ArticleDTO> getArticleList(int boa_no) throws Exception;

	ArticleDTO getArticle(long art_no) throws Exception;

	int updateReadcnt(long art_no) throws Exception;

	int deleteArticle(ArticleDTO articleDTO) throws Exception;

	int updateArticle(ArticleDTO articleDTO) throws Exception;
	
	void insertComment(CommentDTO commentDTO) throws SQLException;
	List<CommentDTO> getCommentList(CommentDTO commentDTO) throws SQLException;
	void deleteComment(CommentDTO commentDTO) throws SQLException;
	int updateComment(CommentDTO commentDTO) throws SQLException;

}
