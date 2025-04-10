# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisForwarding:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_name': 'str',
        'project_id': 'str',
        'stream_name': 'str',
        'stream_id': 'str'
    }

    attribute_map = {
        'region_name': 'region_name',
        'project_id': 'project_id',
        'stream_name': 'stream_name',
        'stream_id': 'stream_id'
    }

    def __init__(self, region_name=None, project_id=None, stream_name=None, stream_id=None):
        r"""DisForwarding

        The model defined in huaweicloud sdk

        :param region_name: **参数说明**：DIS服务对应的region区域
        :type region_name: str
        :param project_id: **参数说明**：DIS服务对应的projectId信息
        :type project_id: str
        :param stream_name: **参数说明**：DIS服务对应的通道名称，stream_id和stream_name两个参数必须携带一个，优先使用stream_id
        :type stream_name: str
        :param stream_id: **参数说明**：DIS服务对应的通道ID，stream_id和stream_name两个参数必须携带一个，优先使用stream_id
        :type stream_id: str
        """
        
        

        self._region_name = None
        self._project_id = None
        self._stream_name = None
        self._stream_id = None
        self.discriminator = None

        self.region_name = region_name
        self.project_id = project_id
        if stream_name is not None:
            self.stream_name = stream_name
        if stream_id is not None:
            self.stream_id = stream_id

    @property
    def region_name(self):
        r"""Gets the region_name of this DisForwarding.

        **参数说明**：DIS服务对应的region区域

        :return: The region_name of this DisForwarding.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this DisForwarding.

        **参数说明**：DIS服务对应的region区域

        :param region_name: The region_name of this DisForwarding.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        r"""Gets the project_id of this DisForwarding.

        **参数说明**：DIS服务对应的projectId信息

        :return: The project_id of this DisForwarding.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DisForwarding.

        **参数说明**：DIS服务对应的projectId信息

        :param project_id: The project_id of this DisForwarding.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def stream_name(self):
        r"""Gets the stream_name of this DisForwarding.

        **参数说明**：DIS服务对应的通道名称，stream_id和stream_name两个参数必须携带一个，优先使用stream_id

        :return: The stream_name of this DisForwarding.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this DisForwarding.

        **参数说明**：DIS服务对应的通道名称，stream_id和stream_name两个参数必须携带一个，优先使用stream_id

        :param stream_name: The stream_name of this DisForwarding.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def stream_id(self):
        r"""Gets the stream_id of this DisForwarding.

        **参数说明**：DIS服务对应的通道ID，stream_id和stream_name两个参数必须携带一个，优先使用stream_id

        :return: The stream_id of this DisForwarding.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this DisForwarding.

        **参数说明**：DIS服务对应的通道ID，stream_id和stream_name两个参数必须携带一个，优先使用stream_id

        :param stream_id: The stream_id of this DisForwarding.
        :type stream_id: str
        """
        self._stream_id = stream_id

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
        if not isinstance(other, DisForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
