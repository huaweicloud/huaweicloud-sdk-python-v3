# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEnvByNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'environment_name': 'str',
        'region': 'str',
        'component_id': 'str'
    }

    attribute_map = {
        'environment_name': 'environment_name',
        'region': 'region',
        'component_id': 'component_id'
    }

    def __init__(self, environment_name=None, region=None, component_id=None):
        r"""ShowEnvByNameRequest

        The model defined in huaweicloud sdk

        :param environment_name: 环境名称
        :type environment_name: str
        :param region: 环境region
        :type region: str
        :param component_id: 组件id
        :type component_id: str
        """
        
        

        self._environment_name = None
        self._region = None
        self._component_id = None
        self.discriminator = None

        self.environment_name = environment_name
        self.region = region
        self.component_id = component_id

    @property
    def environment_name(self):
        r"""Gets the environment_name of this ShowEnvByNameRequest.

        环境名称

        :return: The environment_name of this ShowEnvByNameRequest.
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        r"""Sets the environment_name of this ShowEnvByNameRequest.

        环境名称

        :param environment_name: The environment_name of this ShowEnvByNameRequest.
        :type environment_name: str
        """
        self._environment_name = environment_name

    @property
    def region(self):
        r"""Gets the region of this ShowEnvByNameRequest.

        环境region

        :return: The region of this ShowEnvByNameRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowEnvByNameRequest.

        环境region

        :param region: The region of this ShowEnvByNameRequest.
        :type region: str
        """
        self._region = region

    @property
    def component_id(self):
        r"""Gets the component_id of this ShowEnvByNameRequest.

        组件id

        :return: The component_id of this ShowEnvByNameRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ShowEnvByNameRequest.

        组件id

        :param component_id: The component_id of this ShowEnvByNameRequest.
        :type component_id: str
        """
        self._component_id = component_id

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
        if not isinstance(other, ShowEnvByNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
