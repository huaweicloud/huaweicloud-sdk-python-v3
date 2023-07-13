# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortalInfosResponseModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'portals': 'list[PortalModel]',
        'page_info': 'PageOffSet'
    }

    attribute_map = {
        'portals': 'portals',
        'page_info': 'page_info'
    }

    def __init__(self, portals=None, page_info=None):
        """ListPortalInfosResponseModel

        The model defined in huaweicloud sdk

        :param portals: 主页列表。
        :type portals: list[:class:`huaweicloudsdkkoomessage.v1.PortalModel`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.PageOffSet`
        """
        
        

        self._portals = None
        self._page_info = None
        self.discriminator = None

        if portals is not None:
            self.portals = portals
        if page_info is not None:
            self.page_info = page_info

    @property
    def portals(self):
        """Gets the portals of this ListPortalInfosResponseModel.

        主页列表。

        :return: The portals of this ListPortalInfosResponseModel.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.PortalModel`]
        """
        return self._portals

    @portals.setter
    def portals(self, portals):
        """Sets the portals of this ListPortalInfosResponseModel.

        主页列表。

        :param portals: The portals of this ListPortalInfosResponseModel.
        :type portals: list[:class:`huaweicloudsdkkoomessage.v1.PortalModel`]
        """
        self._portals = portals

    @property
    def page_info(self):
        """Gets the page_info of this ListPortalInfosResponseModel.

        :return: The page_info of this ListPortalInfosResponseModel.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.PageOffSet`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPortalInfosResponseModel.

        :param page_info: The page_info of this ListPortalInfosResponseModel.
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.PageOffSet`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListPortalInfosResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
