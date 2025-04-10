# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventStreamingCreateReqRuleConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transform': 'TransForm',
        'filter': 'object'
    }

    attribute_map = {
        'transform': 'transform',
        'filter': 'filter'
    }

    def __init__(self, transform=None, filter=None):
        r"""EventStreamingCreateReqRuleConfig

        The model defined in huaweicloud sdk

        :param transform: 
        :type transform: :class:`huaweicloudsdkeg.v1.TransForm`
        :param filter: 过滤规则
        :type filter: object
        """
        
        

        self._transform = None
        self._filter = None
        self.discriminator = None

        if transform is not None:
            self.transform = transform
        if filter is not None:
            self.filter = filter

    @property
    def transform(self):
        r"""Gets the transform of this EventStreamingCreateReqRuleConfig.

        :return: The transform of this EventStreamingCreateReqRuleConfig.
        :rtype: :class:`huaweicloudsdkeg.v1.TransForm`
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        r"""Sets the transform of this EventStreamingCreateReqRuleConfig.

        :param transform: The transform of this EventStreamingCreateReqRuleConfig.
        :type transform: :class:`huaweicloudsdkeg.v1.TransForm`
        """
        self._transform = transform

    @property
    def filter(self):
        r"""Gets the filter of this EventStreamingCreateReqRuleConfig.

        过滤规则

        :return: The filter of this EventStreamingCreateReqRuleConfig.
        :rtype: object
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this EventStreamingCreateReqRuleConfig.

        过滤规则

        :param filter: The filter of this EventStreamingCreateReqRuleConfig.
        :type filter: object
        """
        self._filter = filter

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
        if not isinstance(other, EventStreamingCreateReqRuleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
