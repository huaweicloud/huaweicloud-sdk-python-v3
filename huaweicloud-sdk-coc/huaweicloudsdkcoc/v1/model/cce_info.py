# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CceInfo:

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
        'cce_id': 'str',
        'cce_name': 'str',
        'compliant_count': 'str',
        'non_compliant_count': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cce_id': 'cce_id',
        'cce_name': 'cce_name',
        'compliant_count': 'compliant_count',
        'non_compliant_count': 'non_compliant_count'
    }

    def __init__(self, id=None, cce_id=None, cce_name=None, compliant_count=None, non_compliant_count=None):
        r"""CceInfo

        The model defined in huaweicloud sdk

        :param id: 主键id
        :type id: str
        :param cce_id: cce集群id
        :type cce_id: str
        :param cce_name: cce集群名称
        :type cce_name: str
        :param compliant_count: 合规数量
        :type compliant_count: str
        :param non_compliant_count: 不合规数量
        :type non_compliant_count: str
        """
        
        

        self._id = None
        self._cce_id = None
        self._cce_name = None
        self._compliant_count = None
        self._non_compliant_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cce_id is not None:
            self.cce_id = cce_id
        if cce_name is not None:
            self.cce_name = cce_name
        if compliant_count is not None:
            self.compliant_count = compliant_count
        if non_compliant_count is not None:
            self.non_compliant_count = non_compliant_count

    @property
    def id(self):
        r"""Gets the id of this CceInfo.

        主键id

        :return: The id of this CceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CceInfo.

        主键id

        :param id: The id of this CceInfo.
        :type id: str
        """
        self._id = id

    @property
    def cce_id(self):
        r"""Gets the cce_id of this CceInfo.

        cce集群id

        :return: The cce_id of this CceInfo.
        :rtype: str
        """
        return self._cce_id

    @cce_id.setter
    def cce_id(self, cce_id):
        r"""Sets the cce_id of this CceInfo.

        cce集群id

        :param cce_id: The cce_id of this CceInfo.
        :type cce_id: str
        """
        self._cce_id = cce_id

    @property
    def cce_name(self):
        r"""Gets the cce_name of this CceInfo.

        cce集群名称

        :return: The cce_name of this CceInfo.
        :rtype: str
        """
        return self._cce_name

    @cce_name.setter
    def cce_name(self, cce_name):
        r"""Sets the cce_name of this CceInfo.

        cce集群名称

        :param cce_name: The cce_name of this CceInfo.
        :type cce_name: str
        """
        self._cce_name = cce_name

    @property
    def compliant_count(self):
        r"""Gets the compliant_count of this CceInfo.

        合规数量

        :return: The compliant_count of this CceInfo.
        :rtype: str
        """
        return self._compliant_count

    @compliant_count.setter
    def compliant_count(self, compliant_count):
        r"""Sets the compliant_count of this CceInfo.

        合规数量

        :param compliant_count: The compliant_count of this CceInfo.
        :type compliant_count: str
        """
        self._compliant_count = compliant_count

    @property
    def non_compliant_count(self):
        r"""Gets the non_compliant_count of this CceInfo.

        不合规数量

        :return: The non_compliant_count of this CceInfo.
        :rtype: str
        """
        return self._non_compliant_count

    @non_compliant_count.setter
    def non_compliant_count(self, non_compliant_count):
        r"""Sets the non_compliant_count of this CceInfo.

        不合规数量

        :param non_compliant_count: The non_compliant_count of this CceInfo.
        :type non_compliant_count: str
        """
        self._non_compliant_count = non_compliant_count

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
        if not isinstance(other, CceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
