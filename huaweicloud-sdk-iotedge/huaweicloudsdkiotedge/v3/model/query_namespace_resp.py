# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryNamespaceResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'create_time': 'str',
        'labels': 'dict(str, str)',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'create_time': 'create_time',
        'labels': 'labels',
        'status': 'status'
    }

    def __init__(self, name=None, create_time=None, labels=None, status=None):
        r"""QueryNamespaceResp

        The model defined in huaweicloud sdk

        :param name: 命名空间详情
        :type name: str
        :param create_time: 创建时间
        :type create_time: str
        :param labels: map类型，key为string,value为string
        :type labels: dict(str, str)
        :param status: 命名空间状态
        :type status: str
        """
        
        

        self._name = None
        self._create_time = None
        self._labels = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if create_time is not None:
            self.create_time = create_time
        if labels is not None:
            self.labels = labels
        if status is not None:
            self.status = status

    @property
    def name(self):
        r"""Gets the name of this QueryNamespaceResp.

        命名空间详情

        :return: The name of this QueryNamespaceResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryNamespaceResp.

        命名空间详情

        :param name: The name of this QueryNamespaceResp.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        r"""Gets the create_time of this QueryNamespaceResp.

        创建时间

        :return: The create_time of this QueryNamespaceResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QueryNamespaceResp.

        创建时间

        :param create_time: The create_time of this QueryNamespaceResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def labels(self):
        r"""Gets the labels of this QueryNamespaceResp.

        map类型，key为string,value为string

        :return: The labels of this QueryNamespaceResp.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this QueryNamespaceResp.

        map类型，key为string,value为string

        :param labels: The labels of this QueryNamespaceResp.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def status(self):
        r"""Gets the status of this QueryNamespaceResp.

        命名空间状态

        :return: The status of this QueryNamespaceResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryNamespaceResp.

        命名空间状态

        :param status: The status of this QueryNamespaceResp.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, QueryNamespaceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
