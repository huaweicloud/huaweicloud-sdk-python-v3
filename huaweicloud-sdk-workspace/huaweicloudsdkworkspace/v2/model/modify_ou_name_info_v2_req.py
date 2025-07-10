# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyOuNameInfoV2Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'ou_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ou_name': 'ou_name',
        'description': 'description'
    }

    def __init__(self, id=None, ou_name=None, description=None):
        r"""ModifyOuNameInfoV2Req

        The model defined in huaweicloud sdk

        :param id: ouid。
        :type id: str
        :param ou_name: OU名称。
        :type ou_name: str
        :param description: 描述。
        :type description: str
        """
        
        

        self._id = None
        self._ou_name = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.ou_name = ou_name
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this ModifyOuNameInfoV2Req.

        ouid。

        :return: The id of this ModifyOuNameInfoV2Req.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModifyOuNameInfoV2Req.

        ouid。

        :param id: The id of this ModifyOuNameInfoV2Req.
        :type id: str
        """
        self._id = id

    @property
    def ou_name(self):
        r"""Gets the ou_name of this ModifyOuNameInfoV2Req.

        OU名称。

        :return: The ou_name of this ModifyOuNameInfoV2Req.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this ModifyOuNameInfoV2Req.

        OU名称。

        :param ou_name: The ou_name of this ModifyOuNameInfoV2Req.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def description(self):
        r"""Gets the description of this ModifyOuNameInfoV2Req.

        描述。

        :return: The description of this ModifyOuNameInfoV2Req.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyOuNameInfoV2Req.

        描述。

        :param description: The description of this ModifyOuNameInfoV2Req.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ModifyOuNameInfoV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
