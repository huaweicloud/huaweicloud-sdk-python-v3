# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantDurationCfgResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'basic_min': 'int',
        'basic_max': 'int',
        'basic_advice_value': 'int',
        'middle_min': 'int',
        'middle_max': 'int',
        'middle_advice_value': 'int',
        'advance_min': 'int',
        'advance_max': 'int',
        'advance_advice_value': 'int',
        'flexus_min': 'int',
        'flexus_max': 'int',
        'flexus_advice_value': 'int',
        'cmww_min': 'int',
        'cmww_max': 'int',
        'cmww_advice_value': 'int',
        'ljzn_min': 'int',
        'ljzn_max': 'int',
        'ljzn_advice_value': 'int',
        'short_assess_min': 'int',
        'short_assess_max': 'int'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'basic_min': 'basic_min',
        'basic_max': 'basic_max',
        'basic_advice_value': 'basic_advice_value',
        'middle_min': 'middle_min',
        'middle_max': 'middle_max',
        'middle_advice_value': 'middle_advice_value',
        'advance_min': 'advance_min',
        'advance_max': 'advance_max',
        'advance_advice_value': 'advance_advice_value',
        'flexus_min': 'flexus_min',
        'flexus_max': 'flexus_max',
        'flexus_advice_value': 'flexus_advice_value',
        'cmww_min': 'cmww_min',
        'cmww_max': 'cmww_max',
        'cmww_advice_value': 'cmww_advice_value',
        'ljzn_min': 'ljzn_min',
        'ljzn_max': 'ljzn_max',
        'ljzn_advice_value': 'ljzn_advice_value',
        'short_assess_min': 'short_assess_min',
        'short_assess_max': 'short_assess_max'
    }

    def __init__(self, tenant_id=None, basic_min=None, basic_max=None, basic_advice_value=None, middle_min=None, middle_max=None, middle_advice_value=None, advance_min=None, advance_max=None, advance_advice_value=None, flexus_min=None, flexus_max=None, flexus_advice_value=None, cmww_min=None, cmww_max=None, cmww_advice_value=None, ljzn_min=None, ljzn_max=None, ljzn_advice_value=None, short_assess_min=None, short_assess_max=None):
        r"""ShowTenantDurationCfgResponse

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id
        :type tenant_id: str
        :param basic_min: 基础版最低时长（秒）
        :type basic_min: int
        :param basic_max: 基础版最高时长（秒）
        :type basic_max: int
        :param basic_advice_value: 建议时长（秒）
        :type basic_advice_value: int
        :param middle_min: 进阶版最低时长（秒）
        :type middle_min: int
        :param middle_max: 进阶版最高时长（秒）
        :type middle_max: int
        :param middle_advice_value: 建议时长（秒）
        :type middle_advice_value: int
        :param advance_min: 高级版最低时长（秒）
        :type advance_min: int
        :param advance_max: 高级版最高时长（秒）
        :type advance_max: int
        :param advance_advice_value: 建议时长（秒）
        :type advance_advice_value: int
        :param flexus_min: flexus版最低时长（秒）
        :type flexus_min: int
        :param flexus_max: flexus版最高时长（秒）
        :type flexus_max: int
        :param flexus_advice_value: flexus建议时长（秒）
        :type flexus_advice_value: int
        :param cmww_min: 出门问问最低时长（秒）
        :type cmww_min: int
        :param cmww_max: 出门问问最高时长（秒）
        :type cmww_max: int
        :param cmww_advice_value: 出门问问建议时长（秒）
        :type cmww_advice_value: int
        :param ljzn_min: 逻辑智能最低时长（秒）
        :type ljzn_min: int
        :param ljzn_max: 逻辑智能最高时长（秒）
        :type ljzn_max: int
        :param ljzn_advice_value: 逻辑智能建议时长（秒）
        :type ljzn_advice_value: int
        :param short_assess_min: 短任务质量检测最低时长（秒）
        :type short_assess_min: int
        :param short_assess_max: 短任务质量检测最高时长（秒）
        :type short_assess_max: int
        """
        
        super(ShowTenantDurationCfgResponse, self).__init__()

        self._tenant_id = None
        self._basic_min = None
        self._basic_max = None
        self._basic_advice_value = None
        self._middle_min = None
        self._middle_max = None
        self._middle_advice_value = None
        self._advance_min = None
        self._advance_max = None
        self._advance_advice_value = None
        self._flexus_min = None
        self._flexus_max = None
        self._flexus_advice_value = None
        self._cmww_min = None
        self._cmww_max = None
        self._cmww_advice_value = None
        self._ljzn_min = None
        self._ljzn_max = None
        self._ljzn_advice_value = None
        self._short_assess_min = None
        self._short_assess_max = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if basic_min is not None:
            self.basic_min = basic_min
        if basic_max is not None:
            self.basic_max = basic_max
        if basic_advice_value is not None:
            self.basic_advice_value = basic_advice_value
        if middle_min is not None:
            self.middle_min = middle_min
        if middle_max is not None:
            self.middle_max = middle_max
        if middle_advice_value is not None:
            self.middle_advice_value = middle_advice_value
        if advance_min is not None:
            self.advance_min = advance_min
        if advance_max is not None:
            self.advance_max = advance_max
        if advance_advice_value is not None:
            self.advance_advice_value = advance_advice_value
        if flexus_min is not None:
            self.flexus_min = flexus_min
        if flexus_max is not None:
            self.flexus_max = flexus_max
        if flexus_advice_value is not None:
            self.flexus_advice_value = flexus_advice_value
        if cmww_min is not None:
            self.cmww_min = cmww_min
        if cmww_max is not None:
            self.cmww_max = cmww_max
        if cmww_advice_value is not None:
            self.cmww_advice_value = cmww_advice_value
        if ljzn_min is not None:
            self.ljzn_min = ljzn_min
        if ljzn_max is not None:
            self.ljzn_max = ljzn_max
        if ljzn_advice_value is not None:
            self.ljzn_advice_value = ljzn_advice_value
        if short_assess_min is not None:
            self.short_assess_min = short_assess_min
        if short_assess_max is not None:
            self.short_assess_max = short_assess_max

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowTenantDurationCfgResponse.

        租户id

        :return: The tenant_id of this ShowTenantDurationCfgResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowTenantDurationCfgResponse.

        租户id

        :param tenant_id: The tenant_id of this ShowTenantDurationCfgResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def basic_min(self):
        r"""Gets the basic_min of this ShowTenantDurationCfgResponse.

        基础版最低时长（秒）

        :return: The basic_min of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._basic_min

    @basic_min.setter
    def basic_min(self, basic_min):
        r"""Sets the basic_min of this ShowTenantDurationCfgResponse.

        基础版最低时长（秒）

        :param basic_min: The basic_min of this ShowTenantDurationCfgResponse.
        :type basic_min: int
        """
        self._basic_min = basic_min

    @property
    def basic_max(self):
        r"""Gets the basic_max of this ShowTenantDurationCfgResponse.

        基础版最高时长（秒）

        :return: The basic_max of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._basic_max

    @basic_max.setter
    def basic_max(self, basic_max):
        r"""Sets the basic_max of this ShowTenantDurationCfgResponse.

        基础版最高时长（秒）

        :param basic_max: The basic_max of this ShowTenantDurationCfgResponse.
        :type basic_max: int
        """
        self._basic_max = basic_max

    @property
    def basic_advice_value(self):
        r"""Gets the basic_advice_value of this ShowTenantDurationCfgResponse.

        建议时长（秒）

        :return: The basic_advice_value of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._basic_advice_value

    @basic_advice_value.setter
    def basic_advice_value(self, basic_advice_value):
        r"""Sets the basic_advice_value of this ShowTenantDurationCfgResponse.

        建议时长（秒）

        :param basic_advice_value: The basic_advice_value of this ShowTenantDurationCfgResponse.
        :type basic_advice_value: int
        """
        self._basic_advice_value = basic_advice_value

    @property
    def middle_min(self):
        r"""Gets the middle_min of this ShowTenantDurationCfgResponse.

        进阶版最低时长（秒）

        :return: The middle_min of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._middle_min

    @middle_min.setter
    def middle_min(self, middle_min):
        r"""Sets the middle_min of this ShowTenantDurationCfgResponse.

        进阶版最低时长（秒）

        :param middle_min: The middle_min of this ShowTenantDurationCfgResponse.
        :type middle_min: int
        """
        self._middle_min = middle_min

    @property
    def middle_max(self):
        r"""Gets the middle_max of this ShowTenantDurationCfgResponse.

        进阶版最高时长（秒）

        :return: The middle_max of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._middle_max

    @middle_max.setter
    def middle_max(self, middle_max):
        r"""Sets the middle_max of this ShowTenantDurationCfgResponse.

        进阶版最高时长（秒）

        :param middle_max: The middle_max of this ShowTenantDurationCfgResponse.
        :type middle_max: int
        """
        self._middle_max = middle_max

    @property
    def middle_advice_value(self):
        r"""Gets the middle_advice_value of this ShowTenantDurationCfgResponse.

        建议时长（秒）

        :return: The middle_advice_value of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._middle_advice_value

    @middle_advice_value.setter
    def middle_advice_value(self, middle_advice_value):
        r"""Sets the middle_advice_value of this ShowTenantDurationCfgResponse.

        建议时长（秒）

        :param middle_advice_value: The middle_advice_value of this ShowTenantDurationCfgResponse.
        :type middle_advice_value: int
        """
        self._middle_advice_value = middle_advice_value

    @property
    def advance_min(self):
        r"""Gets the advance_min of this ShowTenantDurationCfgResponse.

        高级版最低时长（秒）

        :return: The advance_min of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._advance_min

    @advance_min.setter
    def advance_min(self, advance_min):
        r"""Sets the advance_min of this ShowTenantDurationCfgResponse.

        高级版最低时长（秒）

        :param advance_min: The advance_min of this ShowTenantDurationCfgResponse.
        :type advance_min: int
        """
        self._advance_min = advance_min

    @property
    def advance_max(self):
        r"""Gets the advance_max of this ShowTenantDurationCfgResponse.

        高级版最高时长（秒）

        :return: The advance_max of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._advance_max

    @advance_max.setter
    def advance_max(self, advance_max):
        r"""Sets the advance_max of this ShowTenantDurationCfgResponse.

        高级版最高时长（秒）

        :param advance_max: The advance_max of this ShowTenantDurationCfgResponse.
        :type advance_max: int
        """
        self._advance_max = advance_max

    @property
    def advance_advice_value(self):
        r"""Gets the advance_advice_value of this ShowTenantDurationCfgResponse.

        建议时长（秒）

        :return: The advance_advice_value of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._advance_advice_value

    @advance_advice_value.setter
    def advance_advice_value(self, advance_advice_value):
        r"""Sets the advance_advice_value of this ShowTenantDurationCfgResponse.

        建议时长（秒）

        :param advance_advice_value: The advance_advice_value of this ShowTenantDurationCfgResponse.
        :type advance_advice_value: int
        """
        self._advance_advice_value = advance_advice_value

    @property
    def flexus_min(self):
        r"""Gets the flexus_min of this ShowTenantDurationCfgResponse.

        flexus版最低时长（秒）

        :return: The flexus_min of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._flexus_min

    @flexus_min.setter
    def flexus_min(self, flexus_min):
        r"""Sets the flexus_min of this ShowTenantDurationCfgResponse.

        flexus版最低时长（秒）

        :param flexus_min: The flexus_min of this ShowTenantDurationCfgResponse.
        :type flexus_min: int
        """
        self._flexus_min = flexus_min

    @property
    def flexus_max(self):
        r"""Gets the flexus_max of this ShowTenantDurationCfgResponse.

        flexus版最高时长（秒）

        :return: The flexus_max of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._flexus_max

    @flexus_max.setter
    def flexus_max(self, flexus_max):
        r"""Sets the flexus_max of this ShowTenantDurationCfgResponse.

        flexus版最高时长（秒）

        :param flexus_max: The flexus_max of this ShowTenantDurationCfgResponse.
        :type flexus_max: int
        """
        self._flexus_max = flexus_max

    @property
    def flexus_advice_value(self):
        r"""Gets the flexus_advice_value of this ShowTenantDurationCfgResponse.

        flexus建议时长（秒）

        :return: The flexus_advice_value of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._flexus_advice_value

    @flexus_advice_value.setter
    def flexus_advice_value(self, flexus_advice_value):
        r"""Sets the flexus_advice_value of this ShowTenantDurationCfgResponse.

        flexus建议时长（秒）

        :param flexus_advice_value: The flexus_advice_value of this ShowTenantDurationCfgResponse.
        :type flexus_advice_value: int
        """
        self._flexus_advice_value = flexus_advice_value

    @property
    def cmww_min(self):
        r"""Gets the cmww_min of this ShowTenantDurationCfgResponse.

        出门问问最低时长（秒）

        :return: The cmww_min of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._cmww_min

    @cmww_min.setter
    def cmww_min(self, cmww_min):
        r"""Sets the cmww_min of this ShowTenantDurationCfgResponse.

        出门问问最低时长（秒）

        :param cmww_min: The cmww_min of this ShowTenantDurationCfgResponse.
        :type cmww_min: int
        """
        self._cmww_min = cmww_min

    @property
    def cmww_max(self):
        r"""Gets the cmww_max of this ShowTenantDurationCfgResponse.

        出门问问最高时长（秒）

        :return: The cmww_max of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._cmww_max

    @cmww_max.setter
    def cmww_max(self, cmww_max):
        r"""Sets the cmww_max of this ShowTenantDurationCfgResponse.

        出门问问最高时长（秒）

        :param cmww_max: The cmww_max of this ShowTenantDurationCfgResponse.
        :type cmww_max: int
        """
        self._cmww_max = cmww_max

    @property
    def cmww_advice_value(self):
        r"""Gets the cmww_advice_value of this ShowTenantDurationCfgResponse.

        出门问问建议时长（秒）

        :return: The cmww_advice_value of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._cmww_advice_value

    @cmww_advice_value.setter
    def cmww_advice_value(self, cmww_advice_value):
        r"""Sets the cmww_advice_value of this ShowTenantDurationCfgResponse.

        出门问问建议时长（秒）

        :param cmww_advice_value: The cmww_advice_value of this ShowTenantDurationCfgResponse.
        :type cmww_advice_value: int
        """
        self._cmww_advice_value = cmww_advice_value

    @property
    def ljzn_min(self):
        r"""Gets the ljzn_min of this ShowTenantDurationCfgResponse.

        逻辑智能最低时长（秒）

        :return: The ljzn_min of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._ljzn_min

    @ljzn_min.setter
    def ljzn_min(self, ljzn_min):
        r"""Sets the ljzn_min of this ShowTenantDurationCfgResponse.

        逻辑智能最低时长（秒）

        :param ljzn_min: The ljzn_min of this ShowTenantDurationCfgResponse.
        :type ljzn_min: int
        """
        self._ljzn_min = ljzn_min

    @property
    def ljzn_max(self):
        r"""Gets the ljzn_max of this ShowTenantDurationCfgResponse.

        逻辑智能最高时长（秒）

        :return: The ljzn_max of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._ljzn_max

    @ljzn_max.setter
    def ljzn_max(self, ljzn_max):
        r"""Sets the ljzn_max of this ShowTenantDurationCfgResponse.

        逻辑智能最高时长（秒）

        :param ljzn_max: The ljzn_max of this ShowTenantDurationCfgResponse.
        :type ljzn_max: int
        """
        self._ljzn_max = ljzn_max

    @property
    def ljzn_advice_value(self):
        r"""Gets the ljzn_advice_value of this ShowTenantDurationCfgResponse.

        逻辑智能建议时长（秒）

        :return: The ljzn_advice_value of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._ljzn_advice_value

    @ljzn_advice_value.setter
    def ljzn_advice_value(self, ljzn_advice_value):
        r"""Sets the ljzn_advice_value of this ShowTenantDurationCfgResponse.

        逻辑智能建议时长（秒）

        :param ljzn_advice_value: The ljzn_advice_value of this ShowTenantDurationCfgResponse.
        :type ljzn_advice_value: int
        """
        self._ljzn_advice_value = ljzn_advice_value

    @property
    def short_assess_min(self):
        r"""Gets the short_assess_min of this ShowTenantDurationCfgResponse.

        短任务质量检测最低时长（秒）

        :return: The short_assess_min of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._short_assess_min

    @short_assess_min.setter
    def short_assess_min(self, short_assess_min):
        r"""Sets the short_assess_min of this ShowTenantDurationCfgResponse.

        短任务质量检测最低时长（秒）

        :param short_assess_min: The short_assess_min of this ShowTenantDurationCfgResponse.
        :type short_assess_min: int
        """
        self._short_assess_min = short_assess_min

    @property
    def short_assess_max(self):
        r"""Gets the short_assess_max of this ShowTenantDurationCfgResponse.

        短任务质量检测最高时长（秒）

        :return: The short_assess_max of this ShowTenantDurationCfgResponse.
        :rtype: int
        """
        return self._short_assess_max

    @short_assess_max.setter
    def short_assess_max(self, short_assess_max):
        r"""Sets the short_assess_max of this ShowTenantDurationCfgResponse.

        短任务质量检测最高时长（秒）

        :param short_assess_max: The short_assess_max of this ShowTenantDurationCfgResponse.
        :type short_assess_max: int
        """
        self._short_assess_max = short_assess_max

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
        if not isinstance(other, ShowTenantDurationCfgResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
