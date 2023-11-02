# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDrugModelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'models': 'list[ModelDto]',
        'count': 'int'
    }

    attribute_map = {
        'models': 'models',
        'count': 'count'
    }

    def __init__(self, models=None, count=None):
        """ListDrugModelResponse

        The model defined in huaweicloud sdk

        :param models: 模型列表
        :type models: list[:class:`huaweicloudsdkeihealth.v1.ModelDto`]
        :param count: 模型总数
        :type count: int
        """
        
        super(ListDrugModelResponse, self).__init__()

        self._models = None
        self._count = None
        self.discriminator = None

        if models is not None:
            self.models = models
        if count is not None:
            self.count = count

    @property
    def models(self):
        """Gets the models of this ListDrugModelResponse.

        模型列表

        :return: The models of this ListDrugModelResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ModelDto`]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this ListDrugModelResponse.

        模型列表

        :param models: The models of this ListDrugModelResponse.
        :type models: list[:class:`huaweicloudsdkeihealth.v1.ModelDto`]
        """
        self._models = models

    @property
    def count(self):
        """Gets the count of this ListDrugModelResponse.

        模型总数

        :return: The count of this ListDrugModelResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDrugModelResponse.

        模型总数

        :param count: The count of this ListDrugModelResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListDrugModelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
