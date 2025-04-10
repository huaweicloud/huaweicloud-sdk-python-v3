# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteDomainSetsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'set_ids': 'list[str]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'set_ids': 'set_ids'
    }

    def __init__(self, object_id=None, set_ids=None):
        r"""BatchDeleteDomainSetsDto

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id
        :type object_id: str
        :param set_ids: 域名组id
        :type set_ids: list[str]
        """
        
        

        self._object_id = None
        self._set_ids = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if set_ids is not None:
            self.set_ids = set_ids

    @property
    def object_id(self):
        r"""Gets the object_id of this BatchDeleteDomainSetsDto.

        防护对象id

        :return: The object_id of this BatchDeleteDomainSetsDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this BatchDeleteDomainSetsDto.

        防护对象id

        :param object_id: The object_id of this BatchDeleteDomainSetsDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def set_ids(self):
        r"""Gets the set_ids of this BatchDeleteDomainSetsDto.

        域名组id

        :return: The set_ids of this BatchDeleteDomainSetsDto.
        :rtype: list[str]
        """
        return self._set_ids

    @set_ids.setter
    def set_ids(self, set_ids):
        r"""Sets the set_ids of this BatchDeleteDomainSetsDto.

        域名组id

        :param set_ids: The set_ids of this BatchDeleteDomainSetsDto.
        :type set_ids: list[str]
        """
        self._set_ids = set_ids

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
        if not isinstance(other, BatchDeleteDomainSetsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
