# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKeypairsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'keypairs': 'list[Keypairs]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'keypairs': 'keypairs',
        'page_info': 'page_info'
    }

    def __init__(self, keypairs=None, page_info=None):
        """ListKeypairsResponse

        The model defined in huaweicloud sdk

        :param keypairs: SSH密钥对信息详情
        :type keypairs: list[:class:`huaweicloudsdkkps.v3.Keypairs`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkps.v3.PageInfo`
        """
        
        super(ListKeypairsResponse, self).__init__()

        self._keypairs = None
        self._page_info = None
        self.discriminator = None

        if keypairs is not None:
            self.keypairs = keypairs
        if page_info is not None:
            self.page_info = page_info

    @property
    def keypairs(self):
        """Gets the keypairs of this ListKeypairsResponse.

        SSH密钥对信息详情

        :return: The keypairs of this ListKeypairsResponse.
        :rtype: list[:class:`huaweicloudsdkkps.v3.Keypairs`]
        """
        return self._keypairs

    @keypairs.setter
    def keypairs(self, keypairs):
        """Sets the keypairs of this ListKeypairsResponse.

        SSH密钥对信息详情

        :param keypairs: The keypairs of this ListKeypairsResponse.
        :type keypairs: list[:class:`huaweicloudsdkkps.v3.Keypairs`]
        """
        self._keypairs = keypairs

    @property
    def page_info(self):
        """Gets the page_info of this ListKeypairsResponse.


        :return: The page_info of this ListKeypairsResponse.
        :rtype: :class:`huaweicloudsdkkps.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListKeypairsResponse.


        :param page_info: The page_info of this ListKeypairsResponse.
        :type page_info: :class:`huaweicloudsdkkps.v3.PageInfo`
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
        if not isinstance(other, ListKeypairsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
