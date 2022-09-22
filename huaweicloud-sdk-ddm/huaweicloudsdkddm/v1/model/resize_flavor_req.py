# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeFlavorReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'group_id': 'str',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'group_id': 'group_id',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, spec_code=None, group_id=None, is_auto_pay=None):
        """ResizeFlavorReq

        The model defined in huaweicloud sdk

        :param spec_code: 变更至新规格的资源规格编码。
        :type spec_code: str
        :param group_id: 实例默认一个组，此时不需要传入该参数。当使用组功能创建多个组时, 需要传入需要规格变更的对应组的group_id。
        :type group_id: str
        :param is_auto_pay: 变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: bool
        """
        
        

        self._spec_code = None
        self._group_id = None
        self._is_auto_pay = None
        self.discriminator = None

        self.spec_code = spec_code
        if group_id is not None:
            self.group_id = group_id
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def spec_code(self):
        """Gets the spec_code of this ResizeFlavorReq.

        变更至新规格的资源规格编码。

        :return: The spec_code of this ResizeFlavorReq.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ResizeFlavorReq.

        变更至新规格的资源规格编码。

        :param spec_code: The spec_code of this ResizeFlavorReq.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def group_id(self):
        """Gets the group_id of this ResizeFlavorReq.

        实例默认一个组，此时不需要传入该参数。当使用组功能创建多个组时, 需要传入需要规格变更的对应组的group_id。

        :return: The group_id of this ResizeFlavorReq.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ResizeFlavorReq.

        实例默认一个组，此时不需要传入该参数。当使用组功能创建多个组时, 需要传入需要规格变更的对应组的group_id。

        :param group_id: The group_id of this ResizeFlavorReq.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ResizeFlavorReq.

        变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this ResizeFlavorReq.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ResizeFlavorReq.

        变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。true，表示自动从账户中支付。false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this ResizeFlavorReq.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, ResizeFlavorReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
