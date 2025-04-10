# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HbaseModifySettingV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parm_name': 'str',
        'new_value': 'str',
        'id': 'str'
    }

    attribute_map = {
        'parm_name': 'parm_name',
        'new_value': 'new_value',
        'id': 'id'
    }

    def __init__(self, parm_name=None, new_value=None, id=None):
        r"""HbaseModifySettingV2

        The model defined in huaweicloud sdk

        :param parm_name: 待修改的参数名
        :type parm_name: str
        :param new_value: 设置的参数值
        :type new_value: str
        :param id: 参数ID，可不传
        :type id: str
        """
        
        

        self._parm_name = None
        self._new_value = None
        self._id = None
        self.discriminator = None

        self.parm_name = parm_name
        self.new_value = new_value
        if id is not None:
            self.id = id

    @property
    def parm_name(self):
        r"""Gets the parm_name of this HbaseModifySettingV2.

        待修改的参数名

        :return: The parm_name of this HbaseModifySettingV2.
        :rtype: str
        """
        return self._parm_name

    @parm_name.setter
    def parm_name(self, parm_name):
        r"""Sets the parm_name of this HbaseModifySettingV2.

        待修改的参数名

        :param parm_name: The parm_name of this HbaseModifySettingV2.
        :type parm_name: str
        """
        self._parm_name = parm_name

    @property
    def new_value(self):
        r"""Gets the new_value of this HbaseModifySettingV2.

        设置的参数值

        :return: The new_value of this HbaseModifySettingV2.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        r"""Sets the new_value of this HbaseModifySettingV2.

        设置的参数值

        :param new_value: The new_value of this HbaseModifySettingV2.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def id(self):
        r"""Gets the id of this HbaseModifySettingV2.

        参数ID，可不传

        :return: The id of this HbaseModifySettingV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HbaseModifySettingV2.

        参数ID，可不传

        :param id: The id of this HbaseModifySettingV2.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, HbaseModifySettingV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
