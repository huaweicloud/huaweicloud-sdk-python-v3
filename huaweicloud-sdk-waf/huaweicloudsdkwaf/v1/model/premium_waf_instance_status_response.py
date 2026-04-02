# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PremiumWafInstanceStatusResponse:

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
        'instance_name': 'str',
        'status': 'int',
        'run_status': 'int',
        'access_status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'instance_name': 'instance_name',
        'status': 'status',
        'run_status': 'run_status',
        'access_status': 'access_status'
    }

    def __init__(self, id=None, instance_name=None, status=None, run_status=None, access_status=None):
        r"""PremiumWafInstanceStatusResponse

        The model defined in huaweicloud sdk

        :param id: 实例id
        :type id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param status: **参数解释：** 实例计费状态 **约束限制：** 不涉及 **取值范围：** - -1 退订 - 0 正常 - 1 冻结 - 2 终止 - 3 受限 **默认取值：** 不涉及
        :type status: int
        :param run_status: **参数解释：** 实例运行状态 **约束限制：** 不涉及 **取值范围：** - 0 创建中 - 1 运行中 - 2 删除中 - 3 已删除 - 4 创建失败 - 5 已冻结 - 6 异常 - 7 更新中 - 8 更新失败 **默认取值：** 不涉及
        :type run_status: int
        :param access_status: **参数解释：** 实例接入状态 **约束限制：** 不涉及 **取值范围：** - 0 未接入 - 1 已接入 - 2 DNS解析异常 **默认取值：** 不涉及
        :type access_status: int
        """
        
        

        self._id = None
        self._instance_name = None
        self._status = None
        self._run_status = None
        self._access_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_name is not None:
            self.instance_name = instance_name
        if status is not None:
            self.status = status
        if run_status is not None:
            self.run_status = run_status
        if access_status is not None:
            self.access_status = access_status

    @property
    def id(self):
        r"""Gets the id of this PremiumWafInstanceStatusResponse.

        实例id

        :return: The id of this PremiumWafInstanceStatusResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PremiumWafInstanceStatusResponse.

        实例id

        :param id: The id of this PremiumWafInstanceStatusResponse.
        :type id: str
        """
        self._id = id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this PremiumWafInstanceStatusResponse.

        实例名称

        :return: The instance_name of this PremiumWafInstanceStatusResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this PremiumWafInstanceStatusResponse.

        实例名称

        :param instance_name: The instance_name of this PremiumWafInstanceStatusResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def status(self):
        r"""Gets the status of this PremiumWafInstanceStatusResponse.

        **参数解释：** 实例计费状态 **约束限制：** 不涉及 **取值范围：** - -1 退订 - 0 正常 - 1 冻结 - 2 终止 - 3 受限 **默认取值：** 不涉及

        :return: The status of this PremiumWafInstanceStatusResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PremiumWafInstanceStatusResponse.

        **参数解释：** 实例计费状态 **约束限制：** 不涉及 **取值范围：** - -1 退订 - 0 正常 - 1 冻结 - 2 终止 - 3 受限 **默认取值：** 不涉及

        :param status: The status of this PremiumWafInstanceStatusResponse.
        :type status: int
        """
        self._status = status

    @property
    def run_status(self):
        r"""Gets the run_status of this PremiumWafInstanceStatusResponse.

        **参数解释：** 实例运行状态 **约束限制：** 不涉及 **取值范围：** - 0 创建中 - 1 运行中 - 2 删除中 - 3 已删除 - 4 创建失败 - 5 已冻结 - 6 异常 - 7 更新中 - 8 更新失败 **默认取值：** 不涉及

        :return: The run_status of this PremiumWafInstanceStatusResponse.
        :rtype: int
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        r"""Sets the run_status of this PremiumWafInstanceStatusResponse.

        **参数解释：** 实例运行状态 **约束限制：** 不涉及 **取值范围：** - 0 创建中 - 1 运行中 - 2 删除中 - 3 已删除 - 4 创建失败 - 5 已冻结 - 6 异常 - 7 更新中 - 8 更新失败 **默认取值：** 不涉及

        :param run_status: The run_status of this PremiumWafInstanceStatusResponse.
        :type run_status: int
        """
        self._run_status = run_status

    @property
    def access_status(self):
        r"""Gets the access_status of this PremiumWafInstanceStatusResponse.

        **参数解释：** 实例接入状态 **约束限制：** 不涉及 **取值范围：** - 0 未接入 - 1 已接入 - 2 DNS解析异常 **默认取值：** 不涉及

        :return: The access_status of this PremiumWafInstanceStatusResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        r"""Sets the access_status of this PremiumWafInstanceStatusResponse.

        **参数解释：** 实例接入状态 **约束限制：** 不涉及 **取值范围：** - 0 未接入 - 1 已接入 - 2 DNS解析异常 **默认取值：** 不涉及

        :param access_status: The access_status of this PremiumWafInstanceStatusResponse.
        :type access_status: int
        """
        self._access_status = access_status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PremiumWafInstanceStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
