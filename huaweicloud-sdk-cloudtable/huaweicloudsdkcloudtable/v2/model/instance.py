# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Instance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'cu_num': 'int',
        'lemon_num': 'int',
        'nics': 'list[Nics]',
        'tsd_num': 'int'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'cu_num': 'cu_num',
        'lemon_num': 'lemon_num',
        'nics': 'nics',
        'tsd_num': 'tsd_num'
    }

    def __init__(self, availability_zone=None, cu_num=None, lemon_num=None, nics=None, tsd_num=None):
        """Instance

        The model defined in huaweicloud sdk

        :param availability_zone: 集群所在可用区的ID。
        :type availability_zone: str
        :param cu_num: CloudTable集群计算单元节点数目，至少为2。
        :type cu_num: int
        :param lemon_num: CloudTable集群Lemon节点数目。
        :type lemon_num: int
        :param nics: 集群所在网络信息。
        :type nics: list[:class:`huaweicloudsdkcloudtable.v2.Nics`]
        :param tsd_num: CloudTable集群TSD节点数目，至少为2。
        :type tsd_num: int
        """
        
        

        self._availability_zone = None
        self._cu_num = None
        self._lemon_num = None
        self._nics = None
        self._tsd_num = None
        self.discriminator = None

        self.availability_zone = availability_zone
        self.cu_num = cu_num
        if lemon_num is not None:
            self.lemon_num = lemon_num
        self.nics = nics
        self.tsd_num = tsd_num

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Instance.

        集群所在可用区的ID。

        :return: The availability_zone of this Instance.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Instance.

        集群所在可用区的ID。

        :param availability_zone: The availability_zone of this Instance.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def cu_num(self):
        """Gets the cu_num of this Instance.

        CloudTable集群计算单元节点数目，至少为2。

        :return: The cu_num of this Instance.
        :rtype: int
        """
        return self._cu_num

    @cu_num.setter
    def cu_num(self, cu_num):
        """Sets the cu_num of this Instance.

        CloudTable集群计算单元节点数目，至少为2。

        :param cu_num: The cu_num of this Instance.
        :type cu_num: int
        """
        self._cu_num = cu_num

    @property
    def lemon_num(self):
        """Gets the lemon_num of this Instance.

        CloudTable集群Lemon节点数目。

        :return: The lemon_num of this Instance.
        :rtype: int
        """
        return self._lemon_num

    @lemon_num.setter
    def lemon_num(self, lemon_num):
        """Sets the lemon_num of this Instance.

        CloudTable集群Lemon节点数目。

        :param lemon_num: The lemon_num of this Instance.
        :type lemon_num: int
        """
        self._lemon_num = lemon_num

    @property
    def nics(self):
        """Gets the nics of this Instance.

        集群所在网络信息。

        :return: The nics of this Instance.
        :rtype: list[:class:`huaweicloudsdkcloudtable.v2.Nics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this Instance.

        集群所在网络信息。

        :param nics: The nics of this Instance.
        :type nics: list[:class:`huaweicloudsdkcloudtable.v2.Nics`]
        """
        self._nics = nics

    @property
    def tsd_num(self):
        """Gets the tsd_num of this Instance.

        CloudTable集群TSD节点数目，至少为2。

        :return: The tsd_num of this Instance.
        :rtype: int
        """
        return self._tsd_num

    @tsd_num.setter
    def tsd_num(self, tsd_num):
        """Sets the tsd_num of this Instance.

        CloudTable集群TSD节点数目，至少为2。

        :param tsd_num: The tsd_num of this Instance.
        :type tsd_num: int
        """
        self._tsd_num = tsd_num

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
        if not isinstance(other, Instance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
