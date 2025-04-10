# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'CreateInstanceDetail',
        'extend_param': 'CreateInstanceExtendParam'
    }

    attribute_map = {
        'instance': 'instance',
        'extend_param': 'extend_param'
    }

    def __init__(self, instance=None, extend_param=None):
        r"""CreateInstanceReq

        The model defined in huaweicloud sdk

        :param instance: 
        :type instance: :class:`huaweicloudsdkddm.v1.CreateInstanceDetail`
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkddm.v1.CreateInstanceExtendParam`
        """
        
        

        self._instance = None
        self._extend_param = None
        self.discriminator = None

        self.instance = instance
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def instance(self):
        r"""Gets the instance of this CreateInstanceReq.

        :return: The instance of this CreateInstanceReq.
        :rtype: :class:`huaweicloudsdkddm.v1.CreateInstanceDetail`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this CreateInstanceReq.

        :param instance: The instance of this CreateInstanceReq.
        :type instance: :class:`huaweicloudsdkddm.v1.CreateInstanceDetail`
        """
        self._instance = instance

    @property
    def extend_param(self):
        r"""Gets the extend_param of this CreateInstanceReq.

        :return: The extend_param of this CreateInstanceReq.
        :rtype: :class:`huaweicloudsdkddm.v1.CreateInstanceExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this CreateInstanceReq.

        :param extend_param: The extend_param of this CreateInstanceReq.
        :type extend_param: :class:`huaweicloudsdkddm.v1.CreateInstanceExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, CreateInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
