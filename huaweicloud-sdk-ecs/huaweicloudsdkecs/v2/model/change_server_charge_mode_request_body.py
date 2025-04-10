# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeServerChargeModeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_ids': 'list[str]',
        'charge_mode': 'str',
        'prepaid_options': 'ChangeServerChargeModePrepaidOption',
        'dry_run': 'bool'
    }

    attribute_map = {
        'server_ids': 'server_ids',
        'charge_mode': 'charge_mode',
        'prepaid_options': 'prepaid_options',
        'dry_run': 'dry_run'
    }

    def __init__(self, server_ids=None, charge_mode=None, prepaid_options=None, dry_run=None):
        r"""ChangeServerChargeModeRequestBody

        The model defined in huaweicloud sdk

        :param server_ids: 云服务器ID列表
        :type server_ids: list[str]
        :param charge_mode: 更换后的计费模式：prePaid包周期计费模式
        :type charge_mode: str
        :param prepaid_options: 
        :type prepaid_options: :class:`huaweicloudsdkecs.v2.ChangeServerChargeModePrepaidOption`
        :param dry_run: 是否预先校验此次请求。 true: 发送检查请求，不触发真正的计费转换操作 false: 发送正常请求，触发计费转换操作。 默认值为false
        :type dry_run: bool
        """
        
        

        self._server_ids = None
        self._charge_mode = None
        self._prepaid_options = None
        self._dry_run = None
        self.discriminator = None

        self.server_ids = server_ids
        self.charge_mode = charge_mode
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def server_ids(self):
        r"""Gets the server_ids of this ChangeServerChargeModeRequestBody.

        云服务器ID列表

        :return: The server_ids of this ChangeServerChargeModeRequestBody.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        r"""Sets the server_ids of this ChangeServerChargeModeRequestBody.

        云服务器ID列表

        :param server_ids: The server_ids of this ChangeServerChargeModeRequestBody.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ChangeServerChargeModeRequestBody.

        更换后的计费模式：prePaid包周期计费模式

        :return: The charge_mode of this ChangeServerChargeModeRequestBody.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ChangeServerChargeModeRequestBody.

        更换后的计费模式：prePaid包周期计费模式

        :param charge_mode: The charge_mode of this ChangeServerChargeModeRequestBody.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def prepaid_options(self):
        r"""Gets the prepaid_options of this ChangeServerChargeModeRequestBody.

        :return: The prepaid_options of this ChangeServerChargeModeRequestBody.
        :rtype: :class:`huaweicloudsdkecs.v2.ChangeServerChargeModePrepaidOption`
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        r"""Sets the prepaid_options of this ChangeServerChargeModeRequestBody.

        :param prepaid_options: The prepaid_options of this ChangeServerChargeModeRequestBody.
        :type prepaid_options: :class:`huaweicloudsdkecs.v2.ChangeServerChargeModePrepaidOption`
        """
        self._prepaid_options = prepaid_options

    @property
    def dry_run(self):
        r"""Gets the dry_run of this ChangeServerChargeModeRequestBody.

        是否预先校验此次请求。 true: 发送检查请求，不触发真正的计费转换操作 false: 发送正常请求，触发计费转换操作。 默认值为false

        :return: The dry_run of this ChangeServerChargeModeRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this ChangeServerChargeModeRequestBody.

        是否预先校验此次请求。 true: 发送检查请求，不触发真正的计费转换操作 false: 发送正常请求，触发计费转换操作。 默认值为false

        :param dry_run: The dry_run of this ChangeServerChargeModeRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

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
        if not isinstance(other, ChangeServerChargeModeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
