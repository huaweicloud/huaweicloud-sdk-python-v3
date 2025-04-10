# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditLogDownloadLinkRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'node_id': 'str',
        'last_file_name': 'str',
        'limit': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'last_file_name': 'last_file_name',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, x_language=None, instance_id=None, node_id=None, last_file_name=None, limit=None, start_time=None, end_time=None):
        r"""ListAuditLogDownloadLinkRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param node_id: 节点ID。 - 若输入，则只获取该节点的全量SQL下载链接。 - 若不输入，则获取该实例所有节点的全量SQL下载链接。
        :type node_id: str
        :param last_file_name: 上次查询的最后一个文件的文件名。 - 若输入，则从该文件名以后按字典顺序开始查询。 - 若不输入，则从第一个文件开始查询。
        :type last_file_name: str
        :param limit: 一次查询返回的文件数量。  默认值为10，取值范围：1~50之间的整数值。
        :type limit: int
        :param start_time: 开始时间，不得早于实例创建时间。格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type start_time: str
        :param end_time: 结束时间，不得晚于当前时间。格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type end_time: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._node_id = None
        self._last_file_name = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if last_file_name is not None:
            self.last_file_name = last_file_name
        if limit is not None:
            self.limit = limit
        self.start_time = start_time
        self.end_time = end_time

    @property
    def x_language(self):
        r"""Gets the x_language of this ListAuditLogDownloadLinkRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ListAuditLogDownloadLinkRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListAuditLogDownloadLinkRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ListAuditLogDownloadLinkRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAuditLogDownloadLinkRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this ListAuditLogDownloadLinkRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAuditLogDownloadLinkRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ListAuditLogDownloadLinkRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ListAuditLogDownloadLinkRequest.

        节点ID。 - 若输入，则只获取该节点的全量SQL下载链接。 - 若不输入，则获取该实例所有节点的全量SQL下载链接。

        :return: The node_id of this ListAuditLogDownloadLinkRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListAuditLogDownloadLinkRequest.

        节点ID。 - 若输入，则只获取该节点的全量SQL下载链接。 - 若不输入，则获取该实例所有节点的全量SQL下载链接。

        :param node_id: The node_id of this ListAuditLogDownloadLinkRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def last_file_name(self):
        r"""Gets the last_file_name of this ListAuditLogDownloadLinkRequest.

        上次查询的最后一个文件的文件名。 - 若输入，则从该文件名以后按字典顺序开始查询。 - 若不输入，则从第一个文件开始查询。

        :return: The last_file_name of this ListAuditLogDownloadLinkRequest.
        :rtype: str
        """
        return self._last_file_name

    @last_file_name.setter
    def last_file_name(self, last_file_name):
        r"""Sets the last_file_name of this ListAuditLogDownloadLinkRequest.

        上次查询的最后一个文件的文件名。 - 若输入，则从该文件名以后按字典顺序开始查询。 - 若不输入，则从第一个文件开始查询。

        :param last_file_name: The last_file_name of this ListAuditLogDownloadLinkRequest.
        :type last_file_name: str
        """
        self._last_file_name = last_file_name

    @property
    def limit(self):
        r"""Gets the limit of this ListAuditLogDownloadLinkRequest.

        一次查询返回的文件数量。  默认值为10，取值范围：1~50之间的整数值。

        :return: The limit of this ListAuditLogDownloadLinkRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAuditLogDownloadLinkRequest.

        一次查询返回的文件数量。  默认值为10，取值范围：1~50之间的整数值。

        :param limit: The limit of this ListAuditLogDownloadLinkRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_time(self):
        r"""Gets the start_time of this ListAuditLogDownloadLinkRequest.

        开始时间，不得早于实例创建时间。格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The start_time of this ListAuditLogDownloadLinkRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListAuditLogDownloadLinkRequest.

        开始时间，不得早于实例创建时间。格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param start_time: The start_time of this ListAuditLogDownloadLinkRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAuditLogDownloadLinkRequest.

        结束时间，不得晚于当前时间。格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The end_time of this ListAuditLogDownloadLinkRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAuditLogDownloadLinkRequest.

        结束时间，不得晚于当前时间。格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param end_time: The end_time of this ListAuditLogDownloadLinkRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListAuditLogDownloadLinkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
