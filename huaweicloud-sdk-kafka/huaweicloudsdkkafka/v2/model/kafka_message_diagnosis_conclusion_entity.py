# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaMessageDiagnosisConclusionEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'params': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'params': 'params'
    }

    def __init__(self, id=None, params=None):
        r"""KafkaMessageDiagnosisConclusionEntity

        The model defined in huaweicloud sdk

        :param id: 诊断结论ID
        :type id: int
        :param params: 诊断结论参数列表
        :type params: dict(str, str)
        """
        
        

        self._id = None
        self._params = None
        self.discriminator = None

        self.id = id
        if params is not None:
            self.params = params

    @property
    def id(self):
        r"""Gets the id of this KafkaMessageDiagnosisConclusionEntity.

        诊断结论ID

        :return: The id of this KafkaMessageDiagnosisConclusionEntity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KafkaMessageDiagnosisConclusionEntity.

        诊断结论ID

        :param id: The id of this KafkaMessageDiagnosisConclusionEntity.
        :type id: int
        """
        self._id = id

    @property
    def params(self):
        r"""Gets the params of this KafkaMessageDiagnosisConclusionEntity.

        诊断结论参数列表

        :return: The params of this KafkaMessageDiagnosisConclusionEntity.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this KafkaMessageDiagnosisConclusionEntity.

        诊断结论参数列表

        :param params: The params of this KafkaMessageDiagnosisConclusionEntity.
        :type params: dict(str, str)
        """
        self._params = params

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
        if not isinstance(other, KafkaMessageDiagnosisConclusionEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
