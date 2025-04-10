# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetainAllResourcesTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retain_all_resources': 'bool'
    }

    attribute_map = {
        'retain_all_resources': 'retain_all_resources'
    }

    def __init__(self, retain_all_resources=None):
        r"""RetainAllResourcesTypeHolder

        The model defined in huaweicloud sdk

        :param retain_all_resources: 删除资源栈是否保留资源的标志位，如果不传默认为false，即默认不保留资源（删除资源栈后会删除资源栈中的资源）  * DeleteStackEnhanced API中，如果该参数未在RequestBody中给予，则删除时不会保留资源栈中的资源*
        :type retain_all_resources: bool
        """
        
        

        self._retain_all_resources = None
        self.discriminator = None

        if retain_all_resources is not None:
            self.retain_all_resources = retain_all_resources

    @property
    def retain_all_resources(self):
        r"""Gets the retain_all_resources of this RetainAllResourcesTypeHolder.

        删除资源栈是否保留资源的标志位，如果不传默认为false，即默认不保留资源（删除资源栈后会删除资源栈中的资源）  * DeleteStackEnhanced API中，如果该参数未在RequestBody中给予，则删除时不会保留资源栈中的资源*

        :return: The retain_all_resources of this RetainAllResourcesTypeHolder.
        :rtype: bool
        """
        return self._retain_all_resources

    @retain_all_resources.setter
    def retain_all_resources(self, retain_all_resources):
        r"""Sets the retain_all_resources of this RetainAllResourcesTypeHolder.

        删除资源栈是否保留资源的标志位，如果不传默认为false，即默认不保留资源（删除资源栈后会删除资源栈中的资源）  * DeleteStackEnhanced API中，如果该参数未在RequestBody中给予，则删除时不会保留资源栈中的资源*

        :param retain_all_resources: The retain_all_resources of this RetainAllResourcesTypeHolder.
        :type retain_all_resources: bool
        """
        self._retain_all_resources = retain_all_resources

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
        if not isinstance(other, RetainAllResourcesTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
