# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAomMappingRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_batch': 'bool',
        'body': 'AomMappingRequestInfo'
    }

    attribute_map = {
        'is_batch': 'isBatch',
        'body': 'body'
    }

    def __init__(self, is_batch=None, body=None):
        """CreateAomMappingRulesRequest

        The model defined in huaweicloud sdk

        :param is_batch: 是否开启自动映射
        :type is_batch: bool
        :param body: Body of the CreateAomMappingRulesRequest
        :type body: :class:`huaweicloudsdklts.v2.AomMappingRequestInfo`
        """
        
        

        self._is_batch = None
        self._body = None
        self.discriminator = None

        self.is_batch = is_batch
        if body is not None:
            self.body = body

    @property
    def is_batch(self):
        """Gets the is_batch of this CreateAomMappingRulesRequest.

        是否开启自动映射

        :return: The is_batch of this CreateAomMappingRulesRequest.
        :rtype: bool
        """
        return self._is_batch

    @is_batch.setter
    def is_batch(self, is_batch):
        """Sets the is_batch of this CreateAomMappingRulesRequest.

        是否开启自动映射

        :param is_batch: The is_batch of this CreateAomMappingRulesRequest.
        :type is_batch: bool
        """
        self._is_batch = is_batch

    @property
    def body(self):
        """Gets the body of this CreateAomMappingRulesRequest.


        :return: The body of this CreateAomMappingRulesRequest.
        :rtype: :class:`huaweicloudsdklts.v2.AomMappingRequestInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateAomMappingRulesRequest.


        :param body: The body of this CreateAomMappingRulesRequest.
        :type body: :class:`huaweicloudsdklts.v2.AomMappingRequestInfo`
        """
        self._body = body

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
        if not isinstance(other, CreateAomMappingRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
