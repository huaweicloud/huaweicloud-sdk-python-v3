# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamingMediaReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'streaming_play_times': 'int',
        'streaming_error_times': 'int',
        'streaming_success_rate': 'float',
        'sent_packets_per_second': 'float',
        'received_packets_per_second': 'float',
        'recv_packets': 'float',
        'send_packets': 'float',
        'audio_sent_bytes': 'float',
        'audio_rec_bytes': 'float',
        'video_sent_bytes': 'float',
        'video_rec_bytes': 'float',
        'sum_recv_key_frame_delay': 'float',
        'avg_recv_key_frame_delay': 'float',
        'min_recv_key_frame_delay': 'float',
        'max_recv_key_frame_delay': 'float',
        'sum_send_key_frame_delay': 'float',
        'avg_send_key_frame_delay': 'float',
        'min_send_key_frame_delay': 'float',
        'max_send_key_frame_delay': 'float',
        'key_frame_send_cnt': 'float',
        'key_frame_receive_cnt': 'float',
        'tcp_connect_failed': 'float',
        'hand_shake_failed': 'float',
        'rtmp_connect_failed': 'float',
        'create_stream_failed': 'float',
        'play_failed': 'float',
        'publish_failed': 'float',
        'retry_failed': 'float',
        'parse_file_failed': 'float',
        'illegal_url_failed': 'float',
        'illegal_flv_header_failed': 'float',
        'http_timeout_failed': 'float',
        'parse_flv_file_failed': 'float',
        'unknown_failed': 'float'
    }

    attribute_map = {
        'streaming_play_times': 'streamingPlayTimes',
        'streaming_error_times': 'streamingErrorTimes',
        'streaming_success_rate': 'streamingSuccessRate',
        'sent_packets_per_second': 'sentPacketsPerSecond',
        'received_packets_per_second': 'receivedPacketsPerSecond',
        'recv_packets': 'recvPackets',
        'send_packets': 'sendPackets',
        'audio_sent_bytes': 'audioSentBytes',
        'audio_rec_bytes': 'audioRecBytes',
        'video_sent_bytes': 'videoSentBytes',
        'video_rec_bytes': 'videoRecBytes',
        'sum_recv_key_frame_delay': 'sumRecvKeyFrameDelay',
        'avg_recv_key_frame_delay': 'avgRecvKeyFrameDelay',
        'min_recv_key_frame_delay': 'minRecvKeyFrameDelay',
        'max_recv_key_frame_delay': 'maxRecvKeyFrameDelay',
        'sum_send_key_frame_delay': 'sumSendKeyFrameDelay',
        'avg_send_key_frame_delay': 'avgSendKeyFrameDelay',
        'min_send_key_frame_delay': 'minSendKeyFrameDelay',
        'max_send_key_frame_delay': 'maxSendKeyFrameDelay',
        'key_frame_send_cnt': 'keyFrameSendCnt',
        'key_frame_receive_cnt': 'keyFrameReceiveCnt',
        'tcp_connect_failed': 'tcpConnectFailed',
        'hand_shake_failed': 'handShakeFailed',
        'rtmp_connect_failed': 'rtmpConnectFailed',
        'create_stream_failed': 'createStreamFailed',
        'play_failed': 'playFailed',
        'publish_failed': 'publishFailed',
        'retry_failed': 'retryFailed',
        'parse_file_failed': 'parseFileFailed',
        'illegal_url_failed': 'illegalUrlFailed',
        'illegal_flv_header_failed': 'illegalFlvHeaderFailed',
        'http_timeout_failed': 'httpTimeoutFailed',
        'parse_flv_file_failed': 'parseFlvFileFailed',
        'unknown_failed': 'unknownFailed'
    }

    def __init__(self, streaming_play_times=None, streaming_error_times=None, streaming_success_rate=None, sent_packets_per_second=None, received_packets_per_second=None, recv_packets=None, send_packets=None, audio_sent_bytes=None, audio_rec_bytes=None, video_sent_bytes=None, video_rec_bytes=None, sum_recv_key_frame_delay=None, avg_recv_key_frame_delay=None, min_recv_key_frame_delay=None, max_recv_key_frame_delay=None, sum_send_key_frame_delay=None, avg_send_key_frame_delay=None, min_send_key_frame_delay=None, max_send_key_frame_delay=None, key_frame_send_cnt=None, key_frame_receive_cnt=None, tcp_connect_failed=None, hand_shake_failed=None, rtmp_connect_failed=None, create_stream_failed=None, play_failed=None, publish_failed=None, retry_failed=None, parse_file_failed=None, illegal_url_failed=None, illegal_flv_header_failed=None, http_timeout_failed=None, parse_flv_file_failed=None, unknown_failed=None):
        """StreamingMediaReport

        The model defined in huaweicloud sdk

        :param streaming_play_times: 流媒体播放次数(流媒体aw执行次数)
        :type streaming_play_times: int
        :param streaming_error_times: 流媒体播放出现失败的次数(失败的流媒体aw次数)
        :type streaming_error_times: int
        :param streaming_success_rate: 流媒体播放成功率
        :type streaming_success_rate: float
        :param sent_packets_per_second: 每秒发送数据包大小
        :type sent_packets_per_second: float
        :param received_packets_per_second: 每秒接收数据包大小
        :type received_packets_per_second: float
        :param recv_packets: 接收数据包大小
        :type recv_packets: float
        :param send_packets: 发送数据包大小
        :type send_packets: float
        :param audio_sent_bytes: 音频发送字节大小
        :type audio_sent_bytes: float
        :param audio_rec_bytes: 音频接收字节大小
        :type audio_rec_bytes: float
        :param video_sent_bytes: 视频发送字节大小
        :type video_sent_bytes: float
        :param video_rec_bytes: 视频接收字节大小
        :type video_rec_bytes: float
        :param sum_recv_key_frame_delay: 接收关键帧延迟之和
        :type sum_recv_key_frame_delay: float
        :param avg_recv_key_frame_delay: 平均接收关键帧延迟
        :type avg_recv_key_frame_delay: float
        :param min_recv_key_frame_delay: 最小接收关键帧延迟
        :type min_recv_key_frame_delay: float
        :param max_recv_key_frame_delay: 最大接收关键帧延迟
        :type max_recv_key_frame_delay: float
        :param sum_send_key_frame_delay: 发送关键帧延迟之和
        :type sum_send_key_frame_delay: float
        :param avg_send_key_frame_delay: 平均发送关键帧延迟
        :type avg_send_key_frame_delay: float
        :param min_send_key_frame_delay: 最小发送关键帧延迟
        :type min_send_key_frame_delay: float
        :param max_send_key_frame_delay: 最大发送关键帧延迟
        :type max_send_key_frame_delay: float
        :param key_frame_send_cnt: 关键帧发送次数
        :type key_frame_send_cnt: float
        :param key_frame_receive_cnt: 关键帧接收次数
        :type key_frame_receive_cnt: float
        :param tcp_connect_failed: TCP连接失败数
        :type tcp_connect_failed: float
        :param hand_shake_failed: 握手失败数
        :type hand_shake_failed: float
        :param rtmp_connect_failed: RTMP连接失败数
        :type rtmp_connect_failed: float
        :param create_stream_failed: 创建流失败数
        :type create_stream_failed: float
        :param play_failed: 播放失败数
        :type play_failed: float
        :param publish_failed: 发布失败数
        :type publish_failed: float
        :param retry_failed: 重试失败数
        :type retry_failed: float
        :param parse_file_failed: 解析文件失败数
        :type parse_file_failed: float
        :param illegal_url_failed: 非法URL失败数
        :type illegal_url_failed: float
        :param illegal_flv_header_failed: 非法FLV Header失败数
        :type illegal_flv_header_failed: float
        :param http_timeout_failed: HTTP连接超时数
        :type http_timeout_failed: float
        :param parse_flv_file_failed: 解析FLV文件失败数
        :type parse_flv_file_failed: float
        :param unknown_failed: 未知错误数
        :type unknown_failed: float
        """
        
        

        self._streaming_play_times = None
        self._streaming_error_times = None
        self._streaming_success_rate = None
        self._sent_packets_per_second = None
        self._received_packets_per_second = None
        self._recv_packets = None
        self._send_packets = None
        self._audio_sent_bytes = None
        self._audio_rec_bytes = None
        self._video_sent_bytes = None
        self._video_rec_bytes = None
        self._sum_recv_key_frame_delay = None
        self._avg_recv_key_frame_delay = None
        self._min_recv_key_frame_delay = None
        self._max_recv_key_frame_delay = None
        self._sum_send_key_frame_delay = None
        self._avg_send_key_frame_delay = None
        self._min_send_key_frame_delay = None
        self._max_send_key_frame_delay = None
        self._key_frame_send_cnt = None
        self._key_frame_receive_cnt = None
        self._tcp_connect_failed = None
        self._hand_shake_failed = None
        self._rtmp_connect_failed = None
        self._create_stream_failed = None
        self._play_failed = None
        self._publish_failed = None
        self._retry_failed = None
        self._parse_file_failed = None
        self._illegal_url_failed = None
        self._illegal_flv_header_failed = None
        self._http_timeout_failed = None
        self._parse_flv_file_failed = None
        self._unknown_failed = None
        self.discriminator = None

        if streaming_play_times is not None:
            self.streaming_play_times = streaming_play_times
        if streaming_error_times is not None:
            self.streaming_error_times = streaming_error_times
        if streaming_success_rate is not None:
            self.streaming_success_rate = streaming_success_rate
        if sent_packets_per_second is not None:
            self.sent_packets_per_second = sent_packets_per_second
        if received_packets_per_second is not None:
            self.received_packets_per_second = received_packets_per_second
        if recv_packets is not None:
            self.recv_packets = recv_packets
        if send_packets is not None:
            self.send_packets = send_packets
        if audio_sent_bytes is not None:
            self.audio_sent_bytes = audio_sent_bytes
        if audio_rec_bytes is not None:
            self.audio_rec_bytes = audio_rec_bytes
        if video_sent_bytes is not None:
            self.video_sent_bytes = video_sent_bytes
        if video_rec_bytes is not None:
            self.video_rec_bytes = video_rec_bytes
        if sum_recv_key_frame_delay is not None:
            self.sum_recv_key_frame_delay = sum_recv_key_frame_delay
        if avg_recv_key_frame_delay is not None:
            self.avg_recv_key_frame_delay = avg_recv_key_frame_delay
        if min_recv_key_frame_delay is not None:
            self.min_recv_key_frame_delay = min_recv_key_frame_delay
        if max_recv_key_frame_delay is not None:
            self.max_recv_key_frame_delay = max_recv_key_frame_delay
        if sum_send_key_frame_delay is not None:
            self.sum_send_key_frame_delay = sum_send_key_frame_delay
        if avg_send_key_frame_delay is not None:
            self.avg_send_key_frame_delay = avg_send_key_frame_delay
        if min_send_key_frame_delay is not None:
            self.min_send_key_frame_delay = min_send_key_frame_delay
        if max_send_key_frame_delay is not None:
            self.max_send_key_frame_delay = max_send_key_frame_delay
        if key_frame_send_cnt is not None:
            self.key_frame_send_cnt = key_frame_send_cnt
        if key_frame_receive_cnt is not None:
            self.key_frame_receive_cnt = key_frame_receive_cnt
        if tcp_connect_failed is not None:
            self.tcp_connect_failed = tcp_connect_failed
        if hand_shake_failed is not None:
            self.hand_shake_failed = hand_shake_failed
        if rtmp_connect_failed is not None:
            self.rtmp_connect_failed = rtmp_connect_failed
        if create_stream_failed is not None:
            self.create_stream_failed = create_stream_failed
        if play_failed is not None:
            self.play_failed = play_failed
        if publish_failed is not None:
            self.publish_failed = publish_failed
        if retry_failed is not None:
            self.retry_failed = retry_failed
        if parse_file_failed is not None:
            self.parse_file_failed = parse_file_failed
        if illegal_url_failed is not None:
            self.illegal_url_failed = illegal_url_failed
        if illegal_flv_header_failed is not None:
            self.illegal_flv_header_failed = illegal_flv_header_failed
        if http_timeout_failed is not None:
            self.http_timeout_failed = http_timeout_failed
        if parse_flv_file_failed is not None:
            self.parse_flv_file_failed = parse_flv_file_failed
        if unknown_failed is not None:
            self.unknown_failed = unknown_failed

    @property
    def streaming_play_times(self):
        """Gets the streaming_play_times of this StreamingMediaReport.

        流媒体播放次数(流媒体aw执行次数)

        :return: The streaming_play_times of this StreamingMediaReport.
        :rtype: int
        """
        return self._streaming_play_times

    @streaming_play_times.setter
    def streaming_play_times(self, streaming_play_times):
        """Sets the streaming_play_times of this StreamingMediaReport.

        流媒体播放次数(流媒体aw执行次数)

        :param streaming_play_times: The streaming_play_times of this StreamingMediaReport.
        :type streaming_play_times: int
        """
        self._streaming_play_times = streaming_play_times

    @property
    def streaming_error_times(self):
        """Gets the streaming_error_times of this StreamingMediaReport.

        流媒体播放出现失败的次数(失败的流媒体aw次数)

        :return: The streaming_error_times of this StreamingMediaReport.
        :rtype: int
        """
        return self._streaming_error_times

    @streaming_error_times.setter
    def streaming_error_times(self, streaming_error_times):
        """Sets the streaming_error_times of this StreamingMediaReport.

        流媒体播放出现失败的次数(失败的流媒体aw次数)

        :param streaming_error_times: The streaming_error_times of this StreamingMediaReport.
        :type streaming_error_times: int
        """
        self._streaming_error_times = streaming_error_times

    @property
    def streaming_success_rate(self):
        """Gets the streaming_success_rate of this StreamingMediaReport.

        流媒体播放成功率

        :return: The streaming_success_rate of this StreamingMediaReport.
        :rtype: float
        """
        return self._streaming_success_rate

    @streaming_success_rate.setter
    def streaming_success_rate(self, streaming_success_rate):
        """Sets the streaming_success_rate of this StreamingMediaReport.

        流媒体播放成功率

        :param streaming_success_rate: The streaming_success_rate of this StreamingMediaReport.
        :type streaming_success_rate: float
        """
        self._streaming_success_rate = streaming_success_rate

    @property
    def sent_packets_per_second(self):
        """Gets the sent_packets_per_second of this StreamingMediaReport.

        每秒发送数据包大小

        :return: The sent_packets_per_second of this StreamingMediaReport.
        :rtype: float
        """
        return self._sent_packets_per_second

    @sent_packets_per_second.setter
    def sent_packets_per_second(self, sent_packets_per_second):
        """Sets the sent_packets_per_second of this StreamingMediaReport.

        每秒发送数据包大小

        :param sent_packets_per_second: The sent_packets_per_second of this StreamingMediaReport.
        :type sent_packets_per_second: float
        """
        self._sent_packets_per_second = sent_packets_per_second

    @property
    def received_packets_per_second(self):
        """Gets the received_packets_per_second of this StreamingMediaReport.

        每秒接收数据包大小

        :return: The received_packets_per_second of this StreamingMediaReport.
        :rtype: float
        """
        return self._received_packets_per_second

    @received_packets_per_second.setter
    def received_packets_per_second(self, received_packets_per_second):
        """Sets the received_packets_per_second of this StreamingMediaReport.

        每秒接收数据包大小

        :param received_packets_per_second: The received_packets_per_second of this StreamingMediaReport.
        :type received_packets_per_second: float
        """
        self._received_packets_per_second = received_packets_per_second

    @property
    def recv_packets(self):
        """Gets the recv_packets of this StreamingMediaReport.

        接收数据包大小

        :return: The recv_packets of this StreamingMediaReport.
        :rtype: float
        """
        return self._recv_packets

    @recv_packets.setter
    def recv_packets(self, recv_packets):
        """Sets the recv_packets of this StreamingMediaReport.

        接收数据包大小

        :param recv_packets: The recv_packets of this StreamingMediaReport.
        :type recv_packets: float
        """
        self._recv_packets = recv_packets

    @property
    def send_packets(self):
        """Gets the send_packets of this StreamingMediaReport.

        发送数据包大小

        :return: The send_packets of this StreamingMediaReport.
        :rtype: float
        """
        return self._send_packets

    @send_packets.setter
    def send_packets(self, send_packets):
        """Sets the send_packets of this StreamingMediaReport.

        发送数据包大小

        :param send_packets: The send_packets of this StreamingMediaReport.
        :type send_packets: float
        """
        self._send_packets = send_packets

    @property
    def audio_sent_bytes(self):
        """Gets the audio_sent_bytes of this StreamingMediaReport.

        音频发送字节大小

        :return: The audio_sent_bytes of this StreamingMediaReport.
        :rtype: float
        """
        return self._audio_sent_bytes

    @audio_sent_bytes.setter
    def audio_sent_bytes(self, audio_sent_bytes):
        """Sets the audio_sent_bytes of this StreamingMediaReport.

        音频发送字节大小

        :param audio_sent_bytes: The audio_sent_bytes of this StreamingMediaReport.
        :type audio_sent_bytes: float
        """
        self._audio_sent_bytes = audio_sent_bytes

    @property
    def audio_rec_bytes(self):
        """Gets the audio_rec_bytes of this StreamingMediaReport.

        音频接收字节大小

        :return: The audio_rec_bytes of this StreamingMediaReport.
        :rtype: float
        """
        return self._audio_rec_bytes

    @audio_rec_bytes.setter
    def audio_rec_bytes(self, audio_rec_bytes):
        """Sets the audio_rec_bytes of this StreamingMediaReport.

        音频接收字节大小

        :param audio_rec_bytes: The audio_rec_bytes of this StreamingMediaReport.
        :type audio_rec_bytes: float
        """
        self._audio_rec_bytes = audio_rec_bytes

    @property
    def video_sent_bytes(self):
        """Gets the video_sent_bytes of this StreamingMediaReport.

        视频发送字节大小

        :return: The video_sent_bytes of this StreamingMediaReport.
        :rtype: float
        """
        return self._video_sent_bytes

    @video_sent_bytes.setter
    def video_sent_bytes(self, video_sent_bytes):
        """Sets the video_sent_bytes of this StreamingMediaReport.

        视频发送字节大小

        :param video_sent_bytes: The video_sent_bytes of this StreamingMediaReport.
        :type video_sent_bytes: float
        """
        self._video_sent_bytes = video_sent_bytes

    @property
    def video_rec_bytes(self):
        """Gets the video_rec_bytes of this StreamingMediaReport.

        视频接收字节大小

        :return: The video_rec_bytes of this StreamingMediaReport.
        :rtype: float
        """
        return self._video_rec_bytes

    @video_rec_bytes.setter
    def video_rec_bytes(self, video_rec_bytes):
        """Sets the video_rec_bytes of this StreamingMediaReport.

        视频接收字节大小

        :param video_rec_bytes: The video_rec_bytes of this StreamingMediaReport.
        :type video_rec_bytes: float
        """
        self._video_rec_bytes = video_rec_bytes

    @property
    def sum_recv_key_frame_delay(self):
        """Gets the sum_recv_key_frame_delay of this StreamingMediaReport.

        接收关键帧延迟之和

        :return: The sum_recv_key_frame_delay of this StreamingMediaReport.
        :rtype: float
        """
        return self._sum_recv_key_frame_delay

    @sum_recv_key_frame_delay.setter
    def sum_recv_key_frame_delay(self, sum_recv_key_frame_delay):
        """Sets the sum_recv_key_frame_delay of this StreamingMediaReport.

        接收关键帧延迟之和

        :param sum_recv_key_frame_delay: The sum_recv_key_frame_delay of this StreamingMediaReport.
        :type sum_recv_key_frame_delay: float
        """
        self._sum_recv_key_frame_delay = sum_recv_key_frame_delay

    @property
    def avg_recv_key_frame_delay(self):
        """Gets the avg_recv_key_frame_delay of this StreamingMediaReport.

        平均接收关键帧延迟

        :return: The avg_recv_key_frame_delay of this StreamingMediaReport.
        :rtype: float
        """
        return self._avg_recv_key_frame_delay

    @avg_recv_key_frame_delay.setter
    def avg_recv_key_frame_delay(self, avg_recv_key_frame_delay):
        """Sets the avg_recv_key_frame_delay of this StreamingMediaReport.

        平均接收关键帧延迟

        :param avg_recv_key_frame_delay: The avg_recv_key_frame_delay of this StreamingMediaReport.
        :type avg_recv_key_frame_delay: float
        """
        self._avg_recv_key_frame_delay = avg_recv_key_frame_delay

    @property
    def min_recv_key_frame_delay(self):
        """Gets the min_recv_key_frame_delay of this StreamingMediaReport.

        最小接收关键帧延迟

        :return: The min_recv_key_frame_delay of this StreamingMediaReport.
        :rtype: float
        """
        return self._min_recv_key_frame_delay

    @min_recv_key_frame_delay.setter
    def min_recv_key_frame_delay(self, min_recv_key_frame_delay):
        """Sets the min_recv_key_frame_delay of this StreamingMediaReport.

        最小接收关键帧延迟

        :param min_recv_key_frame_delay: The min_recv_key_frame_delay of this StreamingMediaReport.
        :type min_recv_key_frame_delay: float
        """
        self._min_recv_key_frame_delay = min_recv_key_frame_delay

    @property
    def max_recv_key_frame_delay(self):
        """Gets the max_recv_key_frame_delay of this StreamingMediaReport.

        最大接收关键帧延迟

        :return: The max_recv_key_frame_delay of this StreamingMediaReport.
        :rtype: float
        """
        return self._max_recv_key_frame_delay

    @max_recv_key_frame_delay.setter
    def max_recv_key_frame_delay(self, max_recv_key_frame_delay):
        """Sets the max_recv_key_frame_delay of this StreamingMediaReport.

        最大接收关键帧延迟

        :param max_recv_key_frame_delay: The max_recv_key_frame_delay of this StreamingMediaReport.
        :type max_recv_key_frame_delay: float
        """
        self._max_recv_key_frame_delay = max_recv_key_frame_delay

    @property
    def sum_send_key_frame_delay(self):
        """Gets the sum_send_key_frame_delay of this StreamingMediaReport.

        发送关键帧延迟之和

        :return: The sum_send_key_frame_delay of this StreamingMediaReport.
        :rtype: float
        """
        return self._sum_send_key_frame_delay

    @sum_send_key_frame_delay.setter
    def sum_send_key_frame_delay(self, sum_send_key_frame_delay):
        """Sets the sum_send_key_frame_delay of this StreamingMediaReport.

        发送关键帧延迟之和

        :param sum_send_key_frame_delay: The sum_send_key_frame_delay of this StreamingMediaReport.
        :type sum_send_key_frame_delay: float
        """
        self._sum_send_key_frame_delay = sum_send_key_frame_delay

    @property
    def avg_send_key_frame_delay(self):
        """Gets the avg_send_key_frame_delay of this StreamingMediaReport.

        平均发送关键帧延迟

        :return: The avg_send_key_frame_delay of this StreamingMediaReport.
        :rtype: float
        """
        return self._avg_send_key_frame_delay

    @avg_send_key_frame_delay.setter
    def avg_send_key_frame_delay(self, avg_send_key_frame_delay):
        """Sets the avg_send_key_frame_delay of this StreamingMediaReport.

        平均发送关键帧延迟

        :param avg_send_key_frame_delay: The avg_send_key_frame_delay of this StreamingMediaReport.
        :type avg_send_key_frame_delay: float
        """
        self._avg_send_key_frame_delay = avg_send_key_frame_delay

    @property
    def min_send_key_frame_delay(self):
        """Gets the min_send_key_frame_delay of this StreamingMediaReport.

        最小发送关键帧延迟

        :return: The min_send_key_frame_delay of this StreamingMediaReport.
        :rtype: float
        """
        return self._min_send_key_frame_delay

    @min_send_key_frame_delay.setter
    def min_send_key_frame_delay(self, min_send_key_frame_delay):
        """Sets the min_send_key_frame_delay of this StreamingMediaReport.

        最小发送关键帧延迟

        :param min_send_key_frame_delay: The min_send_key_frame_delay of this StreamingMediaReport.
        :type min_send_key_frame_delay: float
        """
        self._min_send_key_frame_delay = min_send_key_frame_delay

    @property
    def max_send_key_frame_delay(self):
        """Gets the max_send_key_frame_delay of this StreamingMediaReport.

        最大发送关键帧延迟

        :return: The max_send_key_frame_delay of this StreamingMediaReport.
        :rtype: float
        """
        return self._max_send_key_frame_delay

    @max_send_key_frame_delay.setter
    def max_send_key_frame_delay(self, max_send_key_frame_delay):
        """Sets the max_send_key_frame_delay of this StreamingMediaReport.

        最大发送关键帧延迟

        :param max_send_key_frame_delay: The max_send_key_frame_delay of this StreamingMediaReport.
        :type max_send_key_frame_delay: float
        """
        self._max_send_key_frame_delay = max_send_key_frame_delay

    @property
    def key_frame_send_cnt(self):
        """Gets the key_frame_send_cnt of this StreamingMediaReport.

        关键帧发送次数

        :return: The key_frame_send_cnt of this StreamingMediaReport.
        :rtype: float
        """
        return self._key_frame_send_cnt

    @key_frame_send_cnt.setter
    def key_frame_send_cnt(self, key_frame_send_cnt):
        """Sets the key_frame_send_cnt of this StreamingMediaReport.

        关键帧发送次数

        :param key_frame_send_cnt: The key_frame_send_cnt of this StreamingMediaReport.
        :type key_frame_send_cnt: float
        """
        self._key_frame_send_cnt = key_frame_send_cnt

    @property
    def key_frame_receive_cnt(self):
        """Gets the key_frame_receive_cnt of this StreamingMediaReport.

        关键帧接收次数

        :return: The key_frame_receive_cnt of this StreamingMediaReport.
        :rtype: float
        """
        return self._key_frame_receive_cnt

    @key_frame_receive_cnt.setter
    def key_frame_receive_cnt(self, key_frame_receive_cnt):
        """Sets the key_frame_receive_cnt of this StreamingMediaReport.

        关键帧接收次数

        :param key_frame_receive_cnt: The key_frame_receive_cnt of this StreamingMediaReport.
        :type key_frame_receive_cnt: float
        """
        self._key_frame_receive_cnt = key_frame_receive_cnt

    @property
    def tcp_connect_failed(self):
        """Gets the tcp_connect_failed of this StreamingMediaReport.

        TCP连接失败数

        :return: The tcp_connect_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._tcp_connect_failed

    @tcp_connect_failed.setter
    def tcp_connect_failed(self, tcp_connect_failed):
        """Sets the tcp_connect_failed of this StreamingMediaReport.

        TCP连接失败数

        :param tcp_connect_failed: The tcp_connect_failed of this StreamingMediaReport.
        :type tcp_connect_failed: float
        """
        self._tcp_connect_failed = tcp_connect_failed

    @property
    def hand_shake_failed(self):
        """Gets the hand_shake_failed of this StreamingMediaReport.

        握手失败数

        :return: The hand_shake_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._hand_shake_failed

    @hand_shake_failed.setter
    def hand_shake_failed(self, hand_shake_failed):
        """Sets the hand_shake_failed of this StreamingMediaReport.

        握手失败数

        :param hand_shake_failed: The hand_shake_failed of this StreamingMediaReport.
        :type hand_shake_failed: float
        """
        self._hand_shake_failed = hand_shake_failed

    @property
    def rtmp_connect_failed(self):
        """Gets the rtmp_connect_failed of this StreamingMediaReport.

        RTMP连接失败数

        :return: The rtmp_connect_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._rtmp_connect_failed

    @rtmp_connect_failed.setter
    def rtmp_connect_failed(self, rtmp_connect_failed):
        """Sets the rtmp_connect_failed of this StreamingMediaReport.

        RTMP连接失败数

        :param rtmp_connect_failed: The rtmp_connect_failed of this StreamingMediaReport.
        :type rtmp_connect_failed: float
        """
        self._rtmp_connect_failed = rtmp_connect_failed

    @property
    def create_stream_failed(self):
        """Gets the create_stream_failed of this StreamingMediaReport.

        创建流失败数

        :return: The create_stream_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._create_stream_failed

    @create_stream_failed.setter
    def create_stream_failed(self, create_stream_failed):
        """Sets the create_stream_failed of this StreamingMediaReport.

        创建流失败数

        :param create_stream_failed: The create_stream_failed of this StreamingMediaReport.
        :type create_stream_failed: float
        """
        self._create_stream_failed = create_stream_failed

    @property
    def play_failed(self):
        """Gets the play_failed of this StreamingMediaReport.

        播放失败数

        :return: The play_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._play_failed

    @play_failed.setter
    def play_failed(self, play_failed):
        """Sets the play_failed of this StreamingMediaReport.

        播放失败数

        :param play_failed: The play_failed of this StreamingMediaReport.
        :type play_failed: float
        """
        self._play_failed = play_failed

    @property
    def publish_failed(self):
        """Gets the publish_failed of this StreamingMediaReport.

        发布失败数

        :return: The publish_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._publish_failed

    @publish_failed.setter
    def publish_failed(self, publish_failed):
        """Sets the publish_failed of this StreamingMediaReport.

        发布失败数

        :param publish_failed: The publish_failed of this StreamingMediaReport.
        :type publish_failed: float
        """
        self._publish_failed = publish_failed

    @property
    def retry_failed(self):
        """Gets the retry_failed of this StreamingMediaReport.

        重试失败数

        :return: The retry_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._retry_failed

    @retry_failed.setter
    def retry_failed(self, retry_failed):
        """Sets the retry_failed of this StreamingMediaReport.

        重试失败数

        :param retry_failed: The retry_failed of this StreamingMediaReport.
        :type retry_failed: float
        """
        self._retry_failed = retry_failed

    @property
    def parse_file_failed(self):
        """Gets the parse_file_failed of this StreamingMediaReport.

        解析文件失败数

        :return: The parse_file_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._parse_file_failed

    @parse_file_failed.setter
    def parse_file_failed(self, parse_file_failed):
        """Sets the parse_file_failed of this StreamingMediaReport.

        解析文件失败数

        :param parse_file_failed: The parse_file_failed of this StreamingMediaReport.
        :type parse_file_failed: float
        """
        self._parse_file_failed = parse_file_failed

    @property
    def illegal_url_failed(self):
        """Gets the illegal_url_failed of this StreamingMediaReport.

        非法URL失败数

        :return: The illegal_url_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._illegal_url_failed

    @illegal_url_failed.setter
    def illegal_url_failed(self, illegal_url_failed):
        """Sets the illegal_url_failed of this StreamingMediaReport.

        非法URL失败数

        :param illegal_url_failed: The illegal_url_failed of this StreamingMediaReport.
        :type illegal_url_failed: float
        """
        self._illegal_url_failed = illegal_url_failed

    @property
    def illegal_flv_header_failed(self):
        """Gets the illegal_flv_header_failed of this StreamingMediaReport.

        非法FLV Header失败数

        :return: The illegal_flv_header_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._illegal_flv_header_failed

    @illegal_flv_header_failed.setter
    def illegal_flv_header_failed(self, illegal_flv_header_failed):
        """Sets the illegal_flv_header_failed of this StreamingMediaReport.

        非法FLV Header失败数

        :param illegal_flv_header_failed: The illegal_flv_header_failed of this StreamingMediaReport.
        :type illegal_flv_header_failed: float
        """
        self._illegal_flv_header_failed = illegal_flv_header_failed

    @property
    def http_timeout_failed(self):
        """Gets the http_timeout_failed of this StreamingMediaReport.

        HTTP连接超时数

        :return: The http_timeout_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._http_timeout_failed

    @http_timeout_failed.setter
    def http_timeout_failed(self, http_timeout_failed):
        """Sets the http_timeout_failed of this StreamingMediaReport.

        HTTP连接超时数

        :param http_timeout_failed: The http_timeout_failed of this StreamingMediaReport.
        :type http_timeout_failed: float
        """
        self._http_timeout_failed = http_timeout_failed

    @property
    def parse_flv_file_failed(self):
        """Gets the parse_flv_file_failed of this StreamingMediaReport.

        解析FLV文件失败数

        :return: The parse_flv_file_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._parse_flv_file_failed

    @parse_flv_file_failed.setter
    def parse_flv_file_failed(self, parse_flv_file_failed):
        """Sets the parse_flv_file_failed of this StreamingMediaReport.

        解析FLV文件失败数

        :param parse_flv_file_failed: The parse_flv_file_failed of this StreamingMediaReport.
        :type parse_flv_file_failed: float
        """
        self._parse_flv_file_failed = parse_flv_file_failed

    @property
    def unknown_failed(self):
        """Gets the unknown_failed of this StreamingMediaReport.

        未知错误数

        :return: The unknown_failed of this StreamingMediaReport.
        :rtype: float
        """
        return self._unknown_failed

    @unknown_failed.setter
    def unknown_failed(self, unknown_failed):
        """Sets the unknown_failed of this StreamingMediaReport.

        未知错误数

        :param unknown_failed: The unknown_failed of this StreamingMediaReport.
        :type unknown_failed: float
        """
        self._unknown_failed = unknown_failed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StreamingMediaReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
