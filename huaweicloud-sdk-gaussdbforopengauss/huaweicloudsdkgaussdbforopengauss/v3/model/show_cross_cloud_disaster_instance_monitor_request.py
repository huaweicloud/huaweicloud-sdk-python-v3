# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCrossCloudDisasterInstanceMonitorRequest:

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
        'disaster_type': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'disaster_type': 'disaster_type'
    }

    def __init__(self, x_language=None, instance_id=None, disaster_type=None):
        r"""ShowCrossCloudDisasterInstanceMonitorRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param instance_id: 实例id。
        :type instance_id: str
        :param disaster_type: 容灾类型
        :type disaster_type: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._disaster_type = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if disaster_type is not None:
            self.disaster_type = disaster_type

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowCrossCloudDisasterInstanceMonitorRequest.

        语言。

        :return: The x_language of this ShowCrossCloudDisasterInstanceMonitorRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowCrossCloudDisasterInstanceMonitorRequest.

        语言。

        :param x_language: The x_language of this ShowCrossCloudDisasterInstanceMonitorRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowCrossCloudDisasterInstanceMonitorRequest.

        实例id。

        :return: The instance_id of this ShowCrossCloudDisasterInstanceMonitorRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowCrossCloudDisasterInstanceMonitorRequest.

        实例id。

        :param instance_id: The instance_id of this ShowCrossCloudDisasterInstanceMonitorRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def disaster_type(self):
        r"""Gets the disaster_type of this ShowCrossCloudDisasterInstanceMonitorRequest.

        容灾类型

        :return: The disaster_type of this ShowCrossCloudDisasterInstanceMonitorRequest.
        :rtype: str
        """
        return self._disaster_type

    @disaster_type.setter
    def disaster_type(self, disaster_type):
        r"""Sets the disaster_type of this ShowCrossCloudDisasterInstanceMonitorRequest.

        容灾类型

        :param disaster_type: The disaster_type of this ShowCrossCloudDisasterInstanceMonitorRequest.
        :type disaster_type: str
        """
        self._disaster_type = disaster_type

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
        if not isinstance(other, ShowCrossCloudDisasterInstanceMonitorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
