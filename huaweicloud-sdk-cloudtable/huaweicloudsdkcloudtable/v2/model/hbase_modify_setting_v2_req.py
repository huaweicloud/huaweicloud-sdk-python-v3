# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HbaseModifySettingV2Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_reboot': 'str',
        'hbase_modify_settings': 'list[HbaseModifySettingV2]'
    }

    attribute_map = {
        'is_reboot': 'is_reboot',
        'hbase_modify_settings': 'hbase_modify_settings'
    }

    def __init__(self, is_reboot=None, hbase_modify_settings=None):
        r"""HbaseModifySettingV2Req

        The model defined in huaweicloud sdk

        :param is_reboot: 是否重启
        :type is_reboot: str
        :param hbase_modify_settings: 参见HBaseModifySettingV2结构说明
        :type hbase_modify_settings: list[:class:`huaweicloudsdkcloudtable.v2.HbaseModifySettingV2`]
        """
        
        

        self._is_reboot = None
        self._hbase_modify_settings = None
        self.discriminator = None

        self.is_reboot = is_reboot
        self.hbase_modify_settings = hbase_modify_settings

    @property
    def is_reboot(self):
        r"""Gets the is_reboot of this HbaseModifySettingV2Req.

        是否重启

        :return: The is_reboot of this HbaseModifySettingV2Req.
        :rtype: str
        """
        return self._is_reboot

    @is_reboot.setter
    def is_reboot(self, is_reboot):
        r"""Sets the is_reboot of this HbaseModifySettingV2Req.

        是否重启

        :param is_reboot: The is_reboot of this HbaseModifySettingV2Req.
        :type is_reboot: str
        """
        self._is_reboot = is_reboot

    @property
    def hbase_modify_settings(self):
        r"""Gets the hbase_modify_settings of this HbaseModifySettingV2Req.

        参见HBaseModifySettingV2结构说明

        :return: The hbase_modify_settings of this HbaseModifySettingV2Req.
        :rtype: list[:class:`huaweicloudsdkcloudtable.v2.HbaseModifySettingV2`]
        """
        return self._hbase_modify_settings

    @hbase_modify_settings.setter
    def hbase_modify_settings(self, hbase_modify_settings):
        r"""Sets the hbase_modify_settings of this HbaseModifySettingV2Req.

        参见HBaseModifySettingV2结构说明

        :param hbase_modify_settings: The hbase_modify_settings of this HbaseModifySettingV2Req.
        :type hbase_modify_settings: list[:class:`huaweicloudsdkcloudtable.v2.HbaseModifySettingV2`]
        """
        self._hbase_modify_settings = hbase_modify_settings

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
        if not isinstance(other, HbaseModifySettingV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
