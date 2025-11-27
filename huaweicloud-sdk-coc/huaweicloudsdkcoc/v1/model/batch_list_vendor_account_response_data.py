# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListVendorAccountResponseData:

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
        'vendor': 'str',
        'account_id': 'str',
        'domain_id': 'str',
        'account_name': 'str',
        'ak': 'str',
        'sync_status': 'str',
        'failure_msg': 'str',
        'sync_date': 'datetime',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'vendor': 'vendor',
        'account_id': 'account_id',
        'domain_id': 'domain_id',
        'account_name': 'account_name',
        'ak': 'ak',
        'sync_status': 'sync_status',
        'failure_msg': 'failure_msg',
        'sync_date': 'sync_date',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, vendor=None, account_id=None, domain_id=None, account_name=None, ak=None, sync_status=None, failure_msg=None, sync_date=None, create_time=None, update_time=None):
        r"""BatchListVendorAccountResponseData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** CMDB分配的云厂商账户ID。 **取值范围：** 不涉及。
        :type id: str
        :param vendor: **参数解释：** 云广商信息。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。
        :type vendor: str
        :param account_id: **参数解释：** 供应商的账户ID。 **取值范围：** 字符串，长度0到64个字符。
        :type account_id: str
        :param domain_id: **参数解释：** 租户id。 **取值范围：** 不涉及。
        :type domain_id: str
        :param account_name: **参数解释：** 账户名。 **取值范围：** 字符串，长度0到64个字符。
        :type account_name: str
        :param ak: **参数解释：** 账户ak。 **取值范围：** 字符串，长度0到64个字符。
        :type ak: str
        :param sync_status: **参数解释：** 任务状态。 **取值范围：** - waiting：待启动。 - running：同步中。 - success：同步成功。 - failed：同步失败。
        :type sync_status: str
        :param failure_msg: **参数解释：** 错误信息。 **取值范围：** 不涉及。
        :type failure_msg: str
        :param sync_date: **参数解释：** 同步时间。 **取值范围：** 不涉及。
        :type sync_date: datetime
        :param create_time: **参数解释：** 创建时间。 **取值范围：** 不涉及。
        :type create_time: datetime
        :param update_time: **参数解释：** 更新时间。 **取值范围：** 不涉及。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._vendor = None
        self._account_id = None
        self._domain_id = None
        self._account_name = None
        self._ak = None
        self._sync_status = None
        self._failure_msg = None
        self._sync_date = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vendor is not None:
            self.vendor = vendor
        if account_id is not None:
            self.account_id = account_id
        if domain_id is not None:
            self.domain_id = domain_id
        if account_name is not None:
            self.account_name = account_name
        if ak is not None:
            self.ak = ak
        if sync_status is not None:
            self.sync_status = sync_status
        if failure_msg is not None:
            self.failure_msg = failure_msg
        if sync_date is not None:
            self.sync_date = sync_date
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this BatchListVendorAccountResponseData.

        **参数解释：** CMDB分配的云厂商账户ID。 **取值范围：** 不涉及。

        :return: The id of this BatchListVendorAccountResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchListVendorAccountResponseData.

        **参数解释：** CMDB分配的云厂商账户ID。 **取值范围：** 不涉及。

        :param id: The id of this BatchListVendorAccountResponseData.
        :type id: str
        """
        self._id = id

    @property
    def vendor(self):
        r"""Gets the vendor of this BatchListVendorAccountResponseData.

        **参数解释：** 云广商信息。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。

        :return: The vendor of this BatchListVendorAccountResponseData.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this BatchListVendorAccountResponseData.

        **参数解释：** 云广商信息。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。

        :param vendor: The vendor of this BatchListVendorAccountResponseData.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def account_id(self):
        r"""Gets the account_id of this BatchListVendorAccountResponseData.

        **参数解释：** 供应商的账户ID。 **取值范围：** 字符串，长度0到64个字符。

        :return: The account_id of this BatchListVendorAccountResponseData.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this BatchListVendorAccountResponseData.

        **参数解释：** 供应商的账户ID。 **取值范围：** 字符串，长度0到64个字符。

        :param account_id: The account_id of this BatchListVendorAccountResponseData.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this BatchListVendorAccountResponseData.

        **参数解释：** 租户id。 **取值范围：** 不涉及。

        :return: The domain_id of this BatchListVendorAccountResponseData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this BatchListVendorAccountResponseData.

        **参数解释：** 租户id。 **取值范围：** 不涉及。

        :param domain_id: The domain_id of this BatchListVendorAccountResponseData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def account_name(self):
        r"""Gets the account_name of this BatchListVendorAccountResponseData.

        **参数解释：** 账户名。 **取值范围：** 字符串，长度0到64个字符。

        :return: The account_name of this BatchListVendorAccountResponseData.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this BatchListVendorAccountResponseData.

        **参数解释：** 账户名。 **取值范围：** 字符串，长度0到64个字符。

        :param account_name: The account_name of this BatchListVendorAccountResponseData.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def ak(self):
        r"""Gets the ak of this BatchListVendorAccountResponseData.

        **参数解释：** 账户ak。 **取值范围：** 字符串，长度0到64个字符。

        :return: The ak of this BatchListVendorAccountResponseData.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this BatchListVendorAccountResponseData.

        **参数解释：** 账户ak。 **取值范围：** 字符串，长度0到64个字符。

        :param ak: The ak of this BatchListVendorAccountResponseData.
        :type ak: str
        """
        self._ak = ak

    @property
    def sync_status(self):
        r"""Gets the sync_status of this BatchListVendorAccountResponseData.

        **参数解释：** 任务状态。 **取值范围：** - waiting：待启动。 - running：同步中。 - success：同步成功。 - failed：同步失败。

        :return: The sync_status of this BatchListVendorAccountResponseData.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        r"""Sets the sync_status of this BatchListVendorAccountResponseData.

        **参数解释：** 任务状态。 **取值范围：** - waiting：待启动。 - running：同步中。 - success：同步成功。 - failed：同步失败。

        :param sync_status: The sync_status of this BatchListVendorAccountResponseData.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def failure_msg(self):
        r"""Gets the failure_msg of this BatchListVendorAccountResponseData.

        **参数解释：** 错误信息。 **取值范围：** 不涉及。

        :return: The failure_msg of this BatchListVendorAccountResponseData.
        :rtype: str
        """
        return self._failure_msg

    @failure_msg.setter
    def failure_msg(self, failure_msg):
        r"""Sets the failure_msg of this BatchListVendorAccountResponseData.

        **参数解释：** 错误信息。 **取值范围：** 不涉及。

        :param failure_msg: The failure_msg of this BatchListVendorAccountResponseData.
        :type failure_msg: str
        """
        self._failure_msg = failure_msg

    @property
    def sync_date(self):
        r"""Gets the sync_date of this BatchListVendorAccountResponseData.

        **参数解释：** 同步时间。 **取值范围：** 不涉及。

        :return: The sync_date of this BatchListVendorAccountResponseData.
        :rtype: datetime
        """
        return self._sync_date

    @sync_date.setter
    def sync_date(self, sync_date):
        r"""Sets the sync_date of this BatchListVendorAccountResponseData.

        **参数解释：** 同步时间。 **取值范围：** 不涉及。

        :param sync_date: The sync_date of this BatchListVendorAccountResponseData.
        :type sync_date: datetime
        """
        self._sync_date = sync_date

    @property
    def create_time(self):
        r"""Gets the create_time of this BatchListVendorAccountResponseData.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :return: The create_time of this BatchListVendorAccountResponseData.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BatchListVendorAccountResponseData.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :param create_time: The create_time of this BatchListVendorAccountResponseData.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this BatchListVendorAccountResponseData.

        **参数解释：** 更新时间。 **取值范围：** 不涉及。

        :return: The update_time of this BatchListVendorAccountResponseData.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this BatchListVendorAccountResponseData.

        **参数解释：** 更新时间。 **取值范围：** 不涉及。

        :param update_time: The update_time of this BatchListVendorAccountResponseData.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, BatchListVendorAccountResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
