# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LocalImageBatchScanRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_all': 'bool',
        'image_info_list': 'list[LocalImageInfo]',
        'image_name': 'str',
        'image_version': 'str',
        'local_image_type': 'str',
        'scan_status': 'str',
        'image_size': 'int',
        'start_latest_update_time': 'int',
        'end_latest_update_time': 'int',
        'start_latest_scan_time': 'int',
        'end_latest_scan_time': 'int'
    }

    attribute_map = {
        'operate_all': 'operate_all',
        'image_info_list': 'image_info_list',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'local_image_type': 'local_image_type',
        'scan_status': 'scan_status',
        'image_size': 'image_size',
        'start_latest_update_time': 'start_latest_update_time',
        'end_latest_update_time': 'end_latest_update_time',
        'start_latest_scan_time': 'start_latest_scan_time',
        'end_latest_scan_time': 'end_latest_scan_time'
    }

    def __init__(self, operate_all=None, image_info_list=None, image_name=None, image_version=None, local_image_type=None, scan_status=None, image_size=None, start_latest_update_time=None, end_latest_update_time=None, start_latest_scan_time=None, end_latest_scan_time=None):
        r"""LocalImageBatchScanRequestBody

        The model defined in huaweicloud sdk

        :param operate_all: 是否扫描全部本地镜像，true扫描所有，非true则不是
        :type operate_all: bool
        :param image_info_list: 需要扫描的本地镜像列表
        :type image_info_list: list[:class:`huaweicloudsdkhss.v5.LocalImageInfo`]
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param local_image_type: 镜像类型，包含如下:   - other_image : 其他镜像   - swr_image : swr镜像仓   
        :type local_image_type: str
        :param scan_status: 扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大
        :type scan_status: str
        :param image_size: 镜像大小
        :type image_size: int
        :param start_latest_update_time: 创建时间开始日期，时间单位：毫秒（ms）
        :type start_latest_update_time: int
        :param end_latest_update_time: 创建时间结束日期，时间单位：毫秒（ms）
        :type end_latest_update_time: int
        :param start_latest_scan_time: 最近一次扫描完成时间开始日期，时间单位：毫秒（ms）
        :type start_latest_scan_time: int
        :param end_latest_scan_time: 最近一次扫描完成时间结束日期，时间单位：毫秒（ms）
        :type end_latest_scan_time: int
        """
        
        

        self._operate_all = None
        self._image_info_list = None
        self._image_name = None
        self._image_version = None
        self._local_image_type = None
        self._scan_status = None
        self._image_size = None
        self._start_latest_update_time = None
        self._end_latest_update_time = None
        self._start_latest_scan_time = None
        self._end_latest_scan_time = None
        self.discriminator = None

        if operate_all is not None:
            self.operate_all = operate_all
        if image_info_list is not None:
            self.image_info_list = image_info_list
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if local_image_type is not None:
            self.local_image_type = local_image_type
        if scan_status is not None:
            self.scan_status = scan_status
        if image_size is not None:
            self.image_size = image_size
        if start_latest_update_time is not None:
            self.start_latest_update_time = start_latest_update_time
        if end_latest_update_time is not None:
            self.end_latest_update_time = end_latest_update_time
        if start_latest_scan_time is not None:
            self.start_latest_scan_time = start_latest_scan_time
        if end_latest_scan_time is not None:
            self.end_latest_scan_time = end_latest_scan_time

    @property
    def operate_all(self):
        r"""Gets the operate_all of this LocalImageBatchScanRequestBody.

        是否扫描全部本地镜像，true扫描所有，非true则不是

        :return: The operate_all of this LocalImageBatchScanRequestBody.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        r"""Sets the operate_all of this LocalImageBatchScanRequestBody.

        是否扫描全部本地镜像，true扫描所有，非true则不是

        :param operate_all: The operate_all of this LocalImageBatchScanRequestBody.
        :type operate_all: bool
        """
        self._operate_all = operate_all

    @property
    def image_info_list(self):
        r"""Gets the image_info_list of this LocalImageBatchScanRequestBody.

        需要扫描的本地镜像列表

        :return: The image_info_list of this LocalImageBatchScanRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.LocalImageInfo`]
        """
        return self._image_info_list

    @image_info_list.setter
    def image_info_list(self, image_info_list):
        r"""Sets the image_info_list of this LocalImageBatchScanRequestBody.

        需要扫描的本地镜像列表

        :param image_info_list: The image_info_list of this LocalImageBatchScanRequestBody.
        :type image_info_list: list[:class:`huaweicloudsdkhss.v5.LocalImageInfo`]
        """
        self._image_info_list = image_info_list

    @property
    def image_name(self):
        r"""Gets the image_name of this LocalImageBatchScanRequestBody.

        镜像名称

        :return: The image_name of this LocalImageBatchScanRequestBody.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this LocalImageBatchScanRequestBody.

        镜像名称

        :param image_name: The image_name of this LocalImageBatchScanRequestBody.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this LocalImageBatchScanRequestBody.

        镜像版本

        :return: The image_version of this LocalImageBatchScanRequestBody.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this LocalImageBatchScanRequestBody.

        镜像版本

        :param image_version: The image_version of this LocalImageBatchScanRequestBody.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def local_image_type(self):
        r"""Gets the local_image_type of this LocalImageBatchScanRequestBody.

        镜像类型，包含如下:   - other_image : 其他镜像   - swr_image : swr镜像仓   

        :return: The local_image_type of this LocalImageBatchScanRequestBody.
        :rtype: str
        """
        return self._local_image_type

    @local_image_type.setter
    def local_image_type(self, local_image_type):
        r"""Sets the local_image_type of this LocalImageBatchScanRequestBody.

        镜像类型，包含如下:   - other_image : 其他镜像   - swr_image : swr镜像仓   

        :param local_image_type: The local_image_type of this LocalImageBatchScanRequestBody.
        :type local_image_type: str
        """
        self._local_image_type = local_image_type

    @property
    def scan_status(self):
        r"""Gets the scan_status of this LocalImageBatchScanRequestBody.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大

        :return: The scan_status of this LocalImageBatchScanRequestBody.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this LocalImageBatchScanRequestBody.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大

        :param scan_status: The scan_status of this LocalImageBatchScanRequestBody.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def image_size(self):
        r"""Gets the image_size of this LocalImageBatchScanRequestBody.

        镜像大小

        :return: The image_size of this LocalImageBatchScanRequestBody.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this LocalImageBatchScanRequestBody.

        镜像大小

        :param image_size: The image_size of this LocalImageBatchScanRequestBody.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def start_latest_update_time(self):
        r"""Gets the start_latest_update_time of this LocalImageBatchScanRequestBody.

        创建时间开始日期，时间单位：毫秒（ms）

        :return: The start_latest_update_time of this LocalImageBatchScanRequestBody.
        :rtype: int
        """
        return self._start_latest_update_time

    @start_latest_update_time.setter
    def start_latest_update_time(self, start_latest_update_time):
        r"""Sets the start_latest_update_time of this LocalImageBatchScanRequestBody.

        创建时间开始日期，时间单位：毫秒（ms）

        :param start_latest_update_time: The start_latest_update_time of this LocalImageBatchScanRequestBody.
        :type start_latest_update_time: int
        """
        self._start_latest_update_time = start_latest_update_time

    @property
    def end_latest_update_time(self):
        r"""Gets the end_latest_update_time of this LocalImageBatchScanRequestBody.

        创建时间结束日期，时间单位：毫秒（ms）

        :return: The end_latest_update_time of this LocalImageBatchScanRequestBody.
        :rtype: int
        """
        return self._end_latest_update_time

    @end_latest_update_time.setter
    def end_latest_update_time(self, end_latest_update_time):
        r"""Sets the end_latest_update_time of this LocalImageBatchScanRequestBody.

        创建时间结束日期，时间单位：毫秒（ms）

        :param end_latest_update_time: The end_latest_update_time of this LocalImageBatchScanRequestBody.
        :type end_latest_update_time: int
        """
        self._end_latest_update_time = end_latest_update_time

    @property
    def start_latest_scan_time(self):
        r"""Gets the start_latest_scan_time of this LocalImageBatchScanRequestBody.

        最近一次扫描完成时间开始日期，时间单位：毫秒（ms）

        :return: The start_latest_scan_time of this LocalImageBatchScanRequestBody.
        :rtype: int
        """
        return self._start_latest_scan_time

    @start_latest_scan_time.setter
    def start_latest_scan_time(self, start_latest_scan_time):
        r"""Sets the start_latest_scan_time of this LocalImageBatchScanRequestBody.

        最近一次扫描完成时间开始日期，时间单位：毫秒（ms）

        :param start_latest_scan_time: The start_latest_scan_time of this LocalImageBatchScanRequestBody.
        :type start_latest_scan_time: int
        """
        self._start_latest_scan_time = start_latest_scan_time

    @property
    def end_latest_scan_time(self):
        r"""Gets the end_latest_scan_time of this LocalImageBatchScanRequestBody.

        最近一次扫描完成时间结束日期，时间单位：毫秒（ms）

        :return: The end_latest_scan_time of this LocalImageBatchScanRequestBody.
        :rtype: int
        """
        return self._end_latest_scan_time

    @end_latest_scan_time.setter
    def end_latest_scan_time(self, end_latest_scan_time):
        r"""Sets the end_latest_scan_time of this LocalImageBatchScanRequestBody.

        最近一次扫描完成时间结束日期，时间单位：毫秒（ms）

        :param end_latest_scan_time: The end_latest_scan_time of this LocalImageBatchScanRequestBody.
        :type end_latest_scan_time: int
        """
        self._end_latest_scan_time = end_latest_scan_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LocalImageBatchScanRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
