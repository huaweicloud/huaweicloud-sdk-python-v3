# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SrFlavorResizeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fe_flavor_id': 'str',
        'be_flavor_id': 'str'
    }

    attribute_map = {
        'fe_flavor_id': 'fe_flavor_id',
        'be_flavor_id': 'be_flavor_id'
    }

    def __init__(self, fe_flavor_id=None, be_flavor_id=None):
        r"""SrFlavorResizeReq

        The model defined in huaweicloud sdk

        :param fe_flavor_id: FE节点CPU、内存规格ID。填空或者不填视为规格ID与原规格ID保持一致。
        :type fe_flavor_id: str
        :param be_flavor_id: BE节点CPU、内存规格ID。填空或者不填视为规格ID与原规格ID保持一致。
        :type be_flavor_id: str
        """
        
        

        self._fe_flavor_id = None
        self._be_flavor_id = None
        self.discriminator = None

        if fe_flavor_id is not None:
            self.fe_flavor_id = fe_flavor_id
        if be_flavor_id is not None:
            self.be_flavor_id = be_flavor_id

    @property
    def fe_flavor_id(self):
        r"""Gets the fe_flavor_id of this SrFlavorResizeReq.

        FE节点CPU、内存规格ID。填空或者不填视为规格ID与原规格ID保持一致。

        :return: The fe_flavor_id of this SrFlavorResizeReq.
        :rtype: str
        """
        return self._fe_flavor_id

    @fe_flavor_id.setter
    def fe_flavor_id(self, fe_flavor_id):
        r"""Sets the fe_flavor_id of this SrFlavorResizeReq.

        FE节点CPU、内存规格ID。填空或者不填视为规格ID与原规格ID保持一致。

        :param fe_flavor_id: The fe_flavor_id of this SrFlavorResizeReq.
        :type fe_flavor_id: str
        """
        self._fe_flavor_id = fe_flavor_id

    @property
    def be_flavor_id(self):
        r"""Gets the be_flavor_id of this SrFlavorResizeReq.

        BE节点CPU、内存规格ID。填空或者不填视为规格ID与原规格ID保持一致。

        :return: The be_flavor_id of this SrFlavorResizeReq.
        :rtype: str
        """
        return self._be_flavor_id

    @be_flavor_id.setter
    def be_flavor_id(self, be_flavor_id):
        r"""Sets the be_flavor_id of this SrFlavorResizeReq.

        BE节点CPU、内存规格ID。填空或者不填视为规格ID与原规格ID保持一致。

        :param be_flavor_id: The be_flavor_id of this SrFlavorResizeReq.
        :type be_flavor_id: str
        """
        self._be_flavor_id = be_flavor_id

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
        if not isinstance(other, SrFlavorResizeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
