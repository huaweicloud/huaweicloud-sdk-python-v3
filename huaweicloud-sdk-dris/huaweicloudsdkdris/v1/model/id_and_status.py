# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdAndStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, id=None, status=None):
        r"""IdAndStatus

        The model defined in huaweicloud sdk

        :param id: **参数说明**：摄像头、雷达或RSU的ID。
        :type id: str
        :param status: **参数说明**：摄像头、雷达或RSU的状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化
        :type status: str
        """
        
        

        self._id = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this IdAndStatus.

        **参数说明**：摄像头、雷达或RSU的ID。

        :return: The id of this IdAndStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IdAndStatus.

        **参数说明**：摄像头、雷达或RSU的ID。

        :param id: The id of this IdAndStatus.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this IdAndStatus.

        **参数说明**：摄像头、雷达或RSU的状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化

        :return: The status of this IdAndStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IdAndStatus.

        **参数说明**：摄像头、雷达或RSU的状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化

        :param status: The status of this IdAndStatus.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, IdAndStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
