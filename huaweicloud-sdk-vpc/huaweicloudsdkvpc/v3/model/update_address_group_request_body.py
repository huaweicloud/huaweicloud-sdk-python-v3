# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAddressGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dry_run': 'bool',
        'address_group': 'UpdateAddressGroupOption'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'address_group': 'address_group'
    }

    def __init__(self, dry_run=None, address_group=None):
        """UpdateAddressGroupRequestBody

        The model defined in huaweicloud sdk

        :param dry_run: 功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会更新地址组内容。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接更新地址组。
        :type dry_run: bool
        :param address_group: 
        :type address_group: :class:`huaweicloudsdkvpc.v3.UpdateAddressGroupOption`
        """
        
        

        self._dry_run = None
        self._address_group = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        self.address_group = address_group

    @property
    def dry_run(self):
        """Gets the dry_run of this UpdateAddressGroupRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会更新地址组内容。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接更新地址组。

        :return: The dry_run of this UpdateAddressGroupRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this UpdateAddressGroupRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会更新地址组内容。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接更新地址组。

        :param dry_run: The dry_run of this UpdateAddressGroupRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def address_group(self):
        """Gets the address_group of this UpdateAddressGroupRequestBody.

        :return: The address_group of this UpdateAddressGroupRequestBody.
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateAddressGroupOption`
        """
        return self._address_group

    @address_group.setter
    def address_group(self, address_group):
        """Sets the address_group of this UpdateAddressGroupRequestBody.

        :param address_group: The address_group of this UpdateAddressGroupRequestBody.
        :type address_group: :class:`huaweicloudsdkvpc.v3.UpdateAddressGroupOption`
        """
        self._address_group = address_group

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
        if not isinstance(other, UpdateAddressGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
