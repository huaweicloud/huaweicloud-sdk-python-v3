# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferAssetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transfer_type': 'str',
        'asset_ids': 'list[str]',
        'dest_project_id': 'str',
        'memo': 'str',
        'auto_accept': 'bool',
        'auto_active': 'bool',
        'is_need_billing': 'bool',
        'transfer_job_id': 'str'
    }

    attribute_map = {
        'transfer_type': 'transfer_type',
        'asset_ids': 'asset_ids',
        'dest_project_id': 'dest_project_id',
        'memo': 'memo',
        'auto_accept': 'auto_accept',
        'auto_active': 'auto_active',
        'is_need_billing': 'is_need_billing',
        'transfer_job_id': 'transfer_job_id'
    }

    def __init__(self, transfer_type=None, asset_ids=None, dest_project_id=None, memo=None, auto_accept=None, auto_active=None, is_need_billing=None, transfer_job_id=None):
        r"""TransferAssetReq

        The model defined in huaweicloud sdk

        :param transfer_type: **参数解释**： 转移类型。默认值是TRANSFER_OUT。 **约束限制**： * 只有管理员或者开了资产转移白名单租户才有权限转出资产。 * 普通租户有权限转回已接收成功的资产，转回给转移发起方。 **取值范围**： * TRANSFER_OUT: 资产转出 * TRANSFER_BACK：资产转回
        :type transfer_type: str
        :param asset_ids: 资产ID列表
        :type asset_ids: list[str]
        :param dest_project_id: 目标用户ID
        :type dest_project_id: str
        :param memo: 备注信息
        :type memo: str
        :param auto_accept: 是否自动接收,管理员可用
        :type auto_accept: bool
        :param auto_active: 是否自动激活,管理员可用
        :type auto_active: bool
        :param is_need_billing: 资产转移时，是否需要从接收方扣减资源（产生计费话单）
        :type is_need_billing: bool
        :param transfer_job_id: 转移任务ID，仅在transfer_type&#x3D;TRANSFER_BACK时需要填写。
        :type transfer_job_id: str
        """
        
        

        self._transfer_type = None
        self._asset_ids = None
        self._dest_project_id = None
        self._memo = None
        self._auto_accept = None
        self._auto_active = None
        self._is_need_billing = None
        self._transfer_job_id = None
        self.discriminator = None

        if transfer_type is not None:
            self.transfer_type = transfer_type
        self.asset_ids = asset_ids
        self.dest_project_id = dest_project_id
        if memo is not None:
            self.memo = memo
        if auto_accept is not None:
            self.auto_accept = auto_accept
        if auto_active is not None:
            self.auto_active = auto_active
        if is_need_billing is not None:
            self.is_need_billing = is_need_billing
        if transfer_job_id is not None:
            self.transfer_job_id = transfer_job_id

    @property
    def transfer_type(self):
        r"""Gets the transfer_type of this TransferAssetReq.

        **参数解释**： 转移类型。默认值是TRANSFER_OUT。 **约束限制**： * 只有管理员或者开了资产转移白名单租户才有权限转出资产。 * 普通租户有权限转回已接收成功的资产，转回给转移发起方。 **取值范围**： * TRANSFER_OUT: 资产转出 * TRANSFER_BACK：资产转回

        :return: The transfer_type of this TransferAssetReq.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        r"""Sets the transfer_type of this TransferAssetReq.

        **参数解释**： 转移类型。默认值是TRANSFER_OUT。 **约束限制**： * 只有管理员或者开了资产转移白名单租户才有权限转出资产。 * 普通租户有权限转回已接收成功的资产，转回给转移发起方。 **取值范围**： * TRANSFER_OUT: 资产转出 * TRANSFER_BACK：资产转回

        :param transfer_type: The transfer_type of this TransferAssetReq.
        :type transfer_type: str
        """
        self._transfer_type = transfer_type

    @property
    def asset_ids(self):
        r"""Gets the asset_ids of this TransferAssetReq.

        资产ID列表

        :return: The asset_ids of this TransferAssetReq.
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        r"""Sets the asset_ids of this TransferAssetReq.

        资产ID列表

        :param asset_ids: The asset_ids of this TransferAssetReq.
        :type asset_ids: list[str]
        """
        self._asset_ids = asset_ids

    @property
    def dest_project_id(self):
        r"""Gets the dest_project_id of this TransferAssetReq.

        目标用户ID

        :return: The dest_project_id of this TransferAssetReq.
        :rtype: str
        """
        return self._dest_project_id

    @dest_project_id.setter
    def dest_project_id(self, dest_project_id):
        r"""Sets the dest_project_id of this TransferAssetReq.

        目标用户ID

        :param dest_project_id: The dest_project_id of this TransferAssetReq.
        :type dest_project_id: str
        """
        self._dest_project_id = dest_project_id

    @property
    def memo(self):
        r"""Gets the memo of this TransferAssetReq.

        备注信息

        :return: The memo of this TransferAssetReq.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        r"""Sets the memo of this TransferAssetReq.

        备注信息

        :param memo: The memo of this TransferAssetReq.
        :type memo: str
        """
        self._memo = memo

    @property
    def auto_accept(self):
        r"""Gets the auto_accept of this TransferAssetReq.

        是否自动接收,管理员可用

        :return: The auto_accept of this TransferAssetReq.
        :rtype: bool
        """
        return self._auto_accept

    @auto_accept.setter
    def auto_accept(self, auto_accept):
        r"""Sets the auto_accept of this TransferAssetReq.

        是否自动接收,管理员可用

        :param auto_accept: The auto_accept of this TransferAssetReq.
        :type auto_accept: bool
        """
        self._auto_accept = auto_accept

    @property
    def auto_active(self):
        r"""Gets the auto_active of this TransferAssetReq.

        是否自动激活,管理员可用

        :return: The auto_active of this TransferAssetReq.
        :rtype: bool
        """
        return self._auto_active

    @auto_active.setter
    def auto_active(self, auto_active):
        r"""Sets the auto_active of this TransferAssetReq.

        是否自动激活,管理员可用

        :param auto_active: The auto_active of this TransferAssetReq.
        :type auto_active: bool
        """
        self._auto_active = auto_active

    @property
    def is_need_billing(self):
        r"""Gets the is_need_billing of this TransferAssetReq.

        资产转移时，是否需要从接收方扣减资源（产生计费话单）

        :return: The is_need_billing of this TransferAssetReq.
        :rtype: bool
        """
        return self._is_need_billing

    @is_need_billing.setter
    def is_need_billing(self, is_need_billing):
        r"""Sets the is_need_billing of this TransferAssetReq.

        资产转移时，是否需要从接收方扣减资源（产生计费话单）

        :param is_need_billing: The is_need_billing of this TransferAssetReq.
        :type is_need_billing: bool
        """
        self._is_need_billing = is_need_billing

    @property
    def transfer_job_id(self):
        r"""Gets the transfer_job_id of this TransferAssetReq.

        转移任务ID，仅在transfer_type=TRANSFER_BACK时需要填写。

        :return: The transfer_job_id of this TransferAssetReq.
        :rtype: str
        """
        return self._transfer_job_id

    @transfer_job_id.setter
    def transfer_job_id(self, transfer_job_id):
        r"""Sets the transfer_job_id of this TransferAssetReq.

        转移任务ID，仅在transfer_type=TRANSFER_BACK时需要填写。

        :param transfer_job_id: The transfer_job_id of this TransferAssetReq.
        :type transfer_job_id: str
        """
        self._transfer_job_id = transfer_job_id

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
        if not isinstance(other, TransferAssetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
