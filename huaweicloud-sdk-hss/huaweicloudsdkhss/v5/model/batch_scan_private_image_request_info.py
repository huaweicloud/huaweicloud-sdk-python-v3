# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchScanPrivateImageRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_type': 'str',
        'image_info_list': 'list[BatchScanSwrImageInfo]',
        'operate_all': 'bool',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'scan_status': 'str',
        'latest_version': 'bool'
    }

    attribute_map = {
        'repo_type': 'repo_type',
        'image_info_list': 'image_info_list',
        'operate_all': 'operate_all',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'scan_status': 'scan_status',
        'latest_version': 'latest_version'
    }

    def __init__(self, repo_type=None, image_info_list=None, operate_all=None, namespace=None, image_name=None, image_version=None, image_type=None, scan_status=None, latest_version=None):
        """BatchScanPrivateImageRequestInfo

        The model defined in huaweicloud sdk

        :param repo_type: 仓库类型，现阶段接入了swr镜像仓库，包含如下:   - SWR : SWR镜像仓库
        :type repo_type: str
        :param image_info_list: 要扫描的镜像信息列表，operate_all参数为false时为必填
        :type image_info_list: list[:class:`huaweicloudsdkhss.v5.BatchScanSwrImageInfo`]
        :param operate_all: 若为true全量查询，可筛选条件全部查询，若image_info_list为空，则必填
        :type operate_all: bool
        :param namespace: 组织名称
        :type namespace: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param image_type: 镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库
        :type image_type: str
        :param scan_status: 扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大
        :type scan_status: str
        :param latest_version: 仅关注最新版本镜像
        :type latest_version: bool
        """
        
        

        self._repo_type = None
        self._image_info_list = None
        self._operate_all = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._scan_status = None
        self._latest_version = None
        self.discriminator = None

        if repo_type is not None:
            self.repo_type = repo_type
        if image_info_list is not None:
            self.image_info_list = image_info_list
        if operate_all is not None:
            self.operate_all = operate_all
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        self.image_type = image_type
        if scan_status is not None:
            self.scan_status = scan_status
        if latest_version is not None:
            self.latest_version = latest_version

    @property
    def repo_type(self):
        """Gets the repo_type of this BatchScanPrivateImageRequestInfo.

        仓库类型，现阶段接入了swr镜像仓库，包含如下:   - SWR : SWR镜像仓库

        :return: The repo_type of this BatchScanPrivateImageRequestInfo.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """Sets the repo_type of this BatchScanPrivateImageRequestInfo.

        仓库类型，现阶段接入了swr镜像仓库，包含如下:   - SWR : SWR镜像仓库

        :param repo_type: The repo_type of this BatchScanPrivateImageRequestInfo.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def image_info_list(self):
        """Gets the image_info_list of this BatchScanPrivateImageRequestInfo.

        要扫描的镜像信息列表，operate_all参数为false时为必填

        :return: The image_info_list of this BatchScanPrivateImageRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.BatchScanSwrImageInfo`]
        """
        return self._image_info_list

    @image_info_list.setter
    def image_info_list(self, image_info_list):
        """Sets the image_info_list of this BatchScanPrivateImageRequestInfo.

        要扫描的镜像信息列表，operate_all参数为false时为必填

        :param image_info_list: The image_info_list of this BatchScanPrivateImageRequestInfo.
        :type image_info_list: list[:class:`huaweicloudsdkhss.v5.BatchScanSwrImageInfo`]
        """
        self._image_info_list = image_info_list

    @property
    def operate_all(self):
        """Gets the operate_all of this BatchScanPrivateImageRequestInfo.

        若为true全量查询，可筛选条件全部查询，若image_info_list为空，则必填

        :return: The operate_all of this BatchScanPrivateImageRequestInfo.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        """Sets the operate_all of this BatchScanPrivateImageRequestInfo.

        若为true全量查询，可筛选条件全部查询，若image_info_list为空，则必填

        :param operate_all: The operate_all of this BatchScanPrivateImageRequestInfo.
        :type operate_all: bool
        """
        self._operate_all = operate_all

    @property
    def namespace(self):
        """Gets the namespace of this BatchScanPrivateImageRequestInfo.

        组织名称

        :return: The namespace of this BatchScanPrivateImageRequestInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BatchScanPrivateImageRequestInfo.

        组织名称

        :param namespace: The namespace of this BatchScanPrivateImageRequestInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        """Gets the image_name of this BatchScanPrivateImageRequestInfo.

        镜像名称

        :return: The image_name of this BatchScanPrivateImageRequestInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this BatchScanPrivateImageRequestInfo.

        镜像名称

        :param image_name: The image_name of this BatchScanPrivateImageRequestInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        """Gets the image_version of this BatchScanPrivateImageRequestInfo.

        镜像版本

        :return: The image_version of this BatchScanPrivateImageRequestInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this BatchScanPrivateImageRequestInfo.

        镜像版本

        :param image_version: The image_version of this BatchScanPrivateImageRequestInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        """Gets the image_type of this BatchScanPrivateImageRequestInfo.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库

        :return: The image_type of this BatchScanPrivateImageRequestInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this BatchScanPrivateImageRequestInfo.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库

        :param image_type: The image_type of this BatchScanPrivateImageRequestInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def scan_status(self):
        """Gets the scan_status of this BatchScanPrivateImageRequestInfo.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大

        :return: The scan_status of this BatchScanPrivateImageRequestInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this BatchScanPrivateImageRequestInfo.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大

        :param scan_status: The scan_status of this BatchScanPrivateImageRequestInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def latest_version(self):
        """Gets the latest_version of this BatchScanPrivateImageRequestInfo.

        仅关注最新版本镜像

        :return: The latest_version of this BatchScanPrivateImageRequestInfo.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this BatchScanPrivateImageRequestInfo.

        仅关注最新版本镜像

        :param latest_version: The latest_version of this BatchScanPrivateImageRequestInfo.
        :type latest_version: bool
        """
        self._latest_version = latest_version

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
        if not isinstance(other, BatchScanPrivateImageRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
