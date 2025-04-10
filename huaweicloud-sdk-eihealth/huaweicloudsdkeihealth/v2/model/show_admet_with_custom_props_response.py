# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAdmetWithCustomPropsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_props': 'list[CustomProp]',
        'props': 'AdmetPropertyDictWithCustom'
    }

    attribute_map = {
        'custom_props': 'custom_props',
        'props': 'props'
    }

    def __init__(self, custom_props=None, props=None):
        r"""ShowAdmetWithCustomPropsResponse

        The model defined in huaweicloud sdk

        :param custom_props: 用户已开启的自定义属性集合
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v2.CustomProp`]
        :param props: 
        :type props: :class:`huaweicloudsdkeihealth.v2.AdmetPropertyDictWithCustom`
        """
        
        super(ShowAdmetWithCustomPropsResponse, self).__init__()

        self._custom_props = None
        self._props = None
        self.discriminator = None

        if custom_props is not None:
            self.custom_props = custom_props
        if props is not None:
            self.props = props

    @property
    def custom_props(self):
        r"""Gets the custom_props of this ShowAdmetWithCustomPropsResponse.

        用户已开启的自定义属性集合

        :return: The custom_props of this ShowAdmetWithCustomPropsResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v2.CustomProp`]
        """
        return self._custom_props

    @custom_props.setter
    def custom_props(self, custom_props):
        r"""Sets the custom_props of this ShowAdmetWithCustomPropsResponse.

        用户已开启的自定义属性集合

        :param custom_props: The custom_props of this ShowAdmetWithCustomPropsResponse.
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v2.CustomProp`]
        """
        self._custom_props = custom_props

    @property
    def props(self):
        r"""Gets the props of this ShowAdmetWithCustomPropsResponse.

        :return: The props of this ShowAdmetWithCustomPropsResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v2.AdmetPropertyDictWithCustom`
        """
        return self._props

    @props.setter
    def props(self, props):
        r"""Sets the props of this ShowAdmetWithCustomPropsResponse.

        :param props: The props of this ShowAdmetWithCustomPropsResponse.
        :type props: :class:`huaweicloudsdkeihealth.v2.AdmetPropertyDictWithCustom`
        """
        self._props = props

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
        if not isinstance(other, ShowAdmetWithCustomPropsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
