# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociatedWikisResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'wikis': 'list[AttachWikiDetail]',
        'total': 'int'
    }

    attribute_map = {
        'wikis': 'wikis',
        'total': 'total'
    }

    def __init__(self, wikis=None, total=None):
        r"""ListAssociatedWikisResponse

        The model defined in huaweicloud sdk

        :param wikis: 关联的wiki列表
        :type wikis: list[:class:`huaweicloudsdkprojectman.v4.AttachWikiDetail`]
        :param total: 总数
        :type total: int
        """
        
        super(ListAssociatedWikisResponse, self).__init__()

        self._wikis = None
        self._total = None
        self.discriminator = None

        if wikis is not None:
            self.wikis = wikis
        if total is not None:
            self.total = total

    @property
    def wikis(self):
        r"""Gets the wikis of this ListAssociatedWikisResponse.

        关联的wiki列表

        :return: The wikis of this ListAssociatedWikisResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.AttachWikiDetail`]
        """
        return self._wikis

    @wikis.setter
    def wikis(self, wikis):
        r"""Sets the wikis of this ListAssociatedWikisResponse.

        关联的wiki列表

        :param wikis: The wikis of this ListAssociatedWikisResponse.
        :type wikis: list[:class:`huaweicloudsdkprojectman.v4.AttachWikiDetail`]
        """
        self._wikis = wikis

    @property
    def total(self):
        r"""Gets the total of this ListAssociatedWikisResponse.

        总数

        :return: The total of this ListAssociatedWikisResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAssociatedWikisResponse.

        总数

        :param total: The total of this ListAssociatedWikisResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAssociatedWikisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
