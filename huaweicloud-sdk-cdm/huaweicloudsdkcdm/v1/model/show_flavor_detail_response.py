# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlavorDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'str_id': 'str',
        'flavor_detail': 'list[FlavorAttribute]'
    }

    attribute_map = {
        'name': 'name',
        'str_id': 'str_id',
        'flavor_detail': 'flavor_detail'
    }

    def __init__(self, name=None, str_id=None, flavor_detail=None):
        r"""ShowFlavorDetailResponse

        The model defined in huaweicloud sdk

        :param name: 规格名称
        :type name: str
        :param str_id: 规格ID
        :type str_id: str
        :param flavor_detail: 规格详细列表
        :type flavor_detail: list[:class:`huaweicloudsdkcdm.v1.FlavorAttribute`]
        """
        
        super(ShowFlavorDetailResponse, self).__init__()

        self._name = None
        self._str_id = None
        self._flavor_detail = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if str_id is not None:
            self.str_id = str_id
        if flavor_detail is not None:
            self.flavor_detail = flavor_detail

    @property
    def name(self):
        r"""Gets the name of this ShowFlavorDetailResponse.

        规格名称

        :return: The name of this ShowFlavorDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowFlavorDetailResponse.

        规格名称

        :param name: The name of this ShowFlavorDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def str_id(self):
        r"""Gets the str_id of this ShowFlavorDetailResponse.

        规格ID

        :return: The str_id of this ShowFlavorDetailResponse.
        :rtype: str
        """
        return self._str_id

    @str_id.setter
    def str_id(self, str_id):
        r"""Sets the str_id of this ShowFlavorDetailResponse.

        规格ID

        :param str_id: The str_id of this ShowFlavorDetailResponse.
        :type str_id: str
        """
        self._str_id = str_id

    @property
    def flavor_detail(self):
        r"""Gets the flavor_detail of this ShowFlavorDetailResponse.

        规格详细列表

        :return: The flavor_detail of this ShowFlavorDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.FlavorAttribute`]
        """
        return self._flavor_detail

    @flavor_detail.setter
    def flavor_detail(self, flavor_detail):
        r"""Sets the flavor_detail of this ShowFlavorDetailResponse.

        规格详细列表

        :param flavor_detail: The flavor_detail of this ShowFlavorDetailResponse.
        :type flavor_detail: list[:class:`huaweicloudsdkcdm.v1.FlavorAttribute`]
        """
        self._flavor_detail = flavor_detail

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
        if not isinstance(other, ShowFlavorDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
