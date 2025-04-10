# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewAgencyLogAccessReqListBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'preview_agency_list': 'list[PreviewAgencyLogAccessReqBody]'
    }

    attribute_map = {
        'preview_agency_list': 'preview_agency_list'
    }

    def __init__(self, preview_agency_list=None):
        r"""PreviewAgencyLogAccessReqListBody

        The model defined in huaweicloud sdk

        :param preview_agency_list: 预览代理列表
        :type preview_agency_list: list[:class:`huaweicloudsdklts.v2.PreviewAgencyLogAccessReqBody`]
        """
        
        

        self._preview_agency_list = None
        self.discriminator = None

        self.preview_agency_list = preview_agency_list

    @property
    def preview_agency_list(self):
        r"""Gets the preview_agency_list of this PreviewAgencyLogAccessReqListBody.

        预览代理列表

        :return: The preview_agency_list of this PreviewAgencyLogAccessReqListBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.PreviewAgencyLogAccessReqBody`]
        """
        return self._preview_agency_list

    @preview_agency_list.setter
    def preview_agency_list(self, preview_agency_list):
        r"""Sets the preview_agency_list of this PreviewAgencyLogAccessReqListBody.

        预览代理列表

        :param preview_agency_list: The preview_agency_list of this PreviewAgencyLogAccessReqListBody.
        :type preview_agency_list: list[:class:`huaweicloudsdklts.v2.PreviewAgencyLogAccessReqBody`]
        """
        self._preview_agency_list = preview_agency_list

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
        if not isinstance(other, PreviewAgencyLogAccessReqListBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
