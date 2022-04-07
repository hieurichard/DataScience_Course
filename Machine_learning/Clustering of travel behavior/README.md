Tên dự án: Phân cụm hành vi di chuyển dựa theo dữ liệu điện thoại

Tổng quan về bộ dữ liệu

Tinh thần của nghề khoa học dữ liệu là khám phá, chinh phục những điều chưa biết và áp dụng những hiểu biết thu được. Trong môi trường học thuật, thật khó để mô phỏng chính xác các nhiệm vụ này. Tuy nhiên, với dự án này, chúng tôi sẽ cố gắng thực hiện một vài thay đổi so với mô hình "sách giáo khoa" truyền thống, để bạn có thể thực sự trải nghiệm được công việc phân tích dữ liệu trong thực tế .

Sau vụ tấn công ngày 11 tháng 9, một loạt các quy định, luật và quy trình đã được ban hành, để có thể bảo vệ tốt hơn các công dân của Hoa Kỳ. Các quy trình này được tiếp nối qua nhiệm kỳ của Tổng thống Bush và được đổi mới, củng cố trong thời kỳ của chính quyền Obama. Sau đó, vào ngày 24 tháng 5 năm 2006, tòa án Giám sát Tình báo Đối ngoại Hoa Kỳ (FISC) đã thực hiện một sự thay đổi cơ bản trong cách tiếp cận Mục 215 của Đạo luật Yêu nước, cho phép FBI bắt buộc phải tạo "hồ sơ nghiệp vụ" liên quan đến các cuộc điều tra khủng bố, được chia sẻ với NSA. Tòa án hiện xác định hồ sơ nghiệm vụ là toàn bộ cơ sở dữ liệu cuộc gọi của một công ty điện thoại, còn được gọi là bản ghi chi tiết cuộc gọi (Call Detail Records - CDR hoặc Metadata - Siêu dữ liệu).

Tin tức về điều này bị đưa ra ánh sáng và công khai sau khi một nhà thầu cũ của NSA làm rò rỉ thông tin, và một vài câu hỏi khác được đặt ra khi phát hiện thêm rằng không chỉ các hồ sơ cuộc gọi của những kẻ khủng bố bị nghi ngờ đang được thu thập hàng loạt ... mà có lẽ là của cả toàn bộ người dân Mỹ. Rốt cuộc, nếu bạn biết ai đó, người đó lại biết một người khác và cứ như thế, hồ sơ cá nhân của bạn có liên quan đến một cuộc điều tra khủng bố. Nhà trắng nhanh chóng trấn an công chúng trong một thông cáo báo chí rằng "Không ai nghe cuộc gọi điện thoại của bạn", bởi vì  "đó không phải là mục đích của chương trình này." Khi đó, công chúng đã được trấn an.

Các câu hỏi bạn sẽ khám phá trong bài tập trong lab này với K-Means là: chính xác siêu dữ liệu điện thoại hữu ích như thế nào? Nó chắc phải có tác dụng nào đó, nếu không, chính phủ sẽ không đầu tư hàng triệu đô vào đó để bí mật thu thập dữ liệu từ các nhà mạng. Ngoài ra loại thông tin tình báo nào bạn có thể trích xuất từ siêu dữ liệu CDR bên cạnh những giá trị bề nổi của nó?

Bạn sẽ sử dụng bộ dữ liệu CDR mẫu được tạo cho 10 người sống ở khu vực đô thị Dallas, Texas. Nhiệm vụ của bạn sẽ là cố gắng thực hiện những gì mà nhiều nhà nghiên cứu đã thực hiện thành công -  khử ẩn danh một phần dữ liệu CDR. Mọi người thường cư xử theo cách có thể dự đoán được, di chuyển từ nhà đi làm và làm một vài việc vặt ở giữa khoảng di chuyển đó. Với đủ dữ liệu cuộc gọi, giả sử có K địa điểm đáng chú ý, K-Means có thể xác định khá dễ dàng các vị trí địa lý nơi một người dành phần lớn thời gian của họ.

Lưu ý: để bảo vệ an toàn, bộ dữ liệu CDR bạn sẽ sử dụng cho bài tập này đã được tạo bằng các công cụ có sẵn trong phần Dive Deeper. CDR ít nhất được cho là được bảo vệ bởi luật riêng tư và là cơ sở để tính doanh thu độc quyền. Trong thực tế, có khá nhiều CDR công khai ngoài kia. Nhiều thông tin có thể được thấy rõ như mạng xã hội, hành vi tội phạm và dù tin hay không, thậm chí là cả sự lây lan của các bệnh như đã được viết trên trang của Flowminder Foundation về Ebola.

Bản ghi chi tiết cuộc gọi (CDR) là bản ghi dữ liệu được tạo bởi một tổng đài điện thoại hoặc các thiết bị viễn thông khác ghi lại những chi tiết của một cuộc gọi điện thoại hoặc giao dịch viễn thông khác (ví dụ: tin nhắn văn bản) đi qua phương tiện hoặc thiết bị đó.

Bản ghi chứa các thuộc tính khác nhau của cuộc gọi, chẳng hạn như thời gian, thời lượng, trạng thái hoàn thành, số nguồn và số đích. Nó tương tự như vé giấy thu phí tự động được các nhà khai thác viết và hẹn giờ cho các cuộc gọi đường dài trong một cuộc trao đổi điện thoại thủ công.

Bộ dữ liệu chúng tôi đã tuyển chọn cho bạn chứa các bản ghi cuộc gọi cho 10 người, được theo dõi trong suốt 3 năm. Công việc của bạn trong dự án này là tìm ra chỗ có thể là nơi ở và làm việc của mỗi người.

Để hoàn thành dự án này, chúng ta cố gắng áp dụng một trong những thuật toán phổ biến nhất trong Phân cụm đã học trong khóa học này: thuật toán k-Means.
