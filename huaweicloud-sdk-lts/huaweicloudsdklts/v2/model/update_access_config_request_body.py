# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccessConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_config_id': 'str',
        'access_config_detail': 'AccessConfigDeatilUpdate',
        'host_group_info': 'AccessConfigHostGroupIdList',
        'access_config_tag': 'list[AccessConfigTag]',
        'log_split': 'bool',
        'binary_collect': 'bool',
        'cluster_id': 'str'
    }

    attribute_map = {
        'access_config_id': 'access_config_id',
        'access_config_detail': 'access_config_detail',
        'host_group_info': 'host_group_info',
        'access_config_tag': 'access_config_tag',
        'log_split': 'log_split',
        'binary_collect': 'binary_collect',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, access_config_id=None, access_config_detail=None, host_group_info=None, access_config_tag=None, log_split=None, binary_collect=None, cluster_id=None):
        """UpdateAccessConfigRequestBody

        The model defined in huaweicloud sdk

        :param access_config_id: 日志接入ID
        :type access_config_id: str
        :param access_config_detail: 
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatilUpdate`
        :param host_group_info: 
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdList`
        :param access_config_tag: 标签信息。KEY不能重复,最多20个标签
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        :param log_split: 日志拆分
        :type log_split: bool
        :param binary_collect: 二进制采集
        :type binary_collect: bool
        :param cluster_id: CCE集群ID，CCE类型时，为必填
        :type cluster_id: str
        """
        
        

        self._access_config_id = None
        self._access_config_detail = None
        self._host_group_info = None
        self._access_config_tag = None
        self._log_split = None
        self._binary_collect = None
        self._cluster_id = None
        self.discriminator = None

        self.access_config_id = access_config_id
        if access_config_detail is not None:
            self.access_config_detail = access_config_detail
        if host_group_info is not None:
            self.host_group_info = host_group_info
        if access_config_tag is not None:
            self.access_config_tag = access_config_tag
        if log_split is not None:
            self.log_split = log_split
        if binary_collect is not None:
            self.binary_collect = binary_collect
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def access_config_id(self):
        """Gets the access_config_id of this UpdateAccessConfigRequestBody.

        日志接入ID

        :return: The access_config_id of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._access_config_id

    @access_config_id.setter
    def access_config_id(self, access_config_id):
        """Sets the access_config_id of this UpdateAccessConfigRequestBody.

        日志接入ID

        :param access_config_id: The access_config_id of this UpdateAccessConfigRequestBody.
        :type access_config_id: str
        """
        self._access_config_id = access_config_id

    @property
    def access_config_detail(self):
        """Gets the access_config_detail of this UpdateAccessConfigRequestBody.

        :return: The access_config_detail of this UpdateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigDeatilUpdate`
        """
        return self._access_config_detail

    @access_config_detail.setter
    def access_config_detail(self, access_config_detail):
        """Sets the access_config_detail of this UpdateAccessConfigRequestBody.

        :param access_config_detail: The access_config_detail of this UpdateAccessConfigRequestBody.
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatilUpdate`
        """
        self._access_config_detail = access_config_detail

    @property
    def host_group_info(self):
        """Gets the host_group_info of this UpdateAccessConfigRequestBody.

        :return: The host_group_info of this UpdateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdList`
        """
        return self._host_group_info

    @host_group_info.setter
    def host_group_info(self, host_group_info):
        """Sets the host_group_info of this UpdateAccessConfigRequestBody.

        :param host_group_info: The host_group_info of this UpdateAccessConfigRequestBody.
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdList`
        """
        self._host_group_info = host_group_info

    @property
    def access_config_tag(self):
        """Gets the access_config_tag of this UpdateAccessConfigRequestBody.

        标签信息。KEY不能重复,最多20个标签

        :return: The access_config_tag of this UpdateAccessConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        return self._access_config_tag

    @access_config_tag.setter
    def access_config_tag(self, access_config_tag):
        """Sets the access_config_tag of this UpdateAccessConfigRequestBody.

        标签信息。KEY不能重复,最多20个标签

        :param access_config_tag: The access_config_tag of this UpdateAccessConfigRequestBody.
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        self._access_config_tag = access_config_tag

    @property
    def log_split(self):
        """Gets the log_split of this UpdateAccessConfigRequestBody.

        日志拆分

        :return: The log_split of this UpdateAccessConfigRequestBody.
        :rtype: bool
        """
        return self._log_split

    @log_split.setter
    def log_split(self, log_split):
        """Sets the log_split of this UpdateAccessConfigRequestBody.

        日志拆分

        :param log_split: The log_split of this UpdateAccessConfigRequestBody.
        :type log_split: bool
        """
        self._log_split = log_split

    @property
    def binary_collect(self):
        """Gets the binary_collect of this UpdateAccessConfigRequestBody.

        二进制采集

        :return: The binary_collect of this UpdateAccessConfigRequestBody.
        :rtype: bool
        """
        return self._binary_collect

    @binary_collect.setter
    def binary_collect(self, binary_collect):
        """Sets the binary_collect of this UpdateAccessConfigRequestBody.

        二进制采集

        :param binary_collect: The binary_collect of this UpdateAccessConfigRequestBody.
        :type binary_collect: bool
        """
        self._binary_collect = binary_collect

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateAccessConfigRequestBody.

        CCE集群ID，CCE类型时，为必填

        :return: The cluster_id of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateAccessConfigRequestBody.

        CCE集群ID，CCE类型时，为必填

        :param cluster_id: The cluster_id of this UpdateAccessConfigRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, UpdateAccessConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
