# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApprovalVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'tenant_id': 'str',
        'name_ch': 'str',
        'name_en': 'str',
        'biz_id': 'int',
        'biz_type': 'BizTypeEnum',
        'biz_info': 'str',
        'biz_info_obj': 'object',
        'biz_version': 'int',
        'biz_status': 'BizStatusEnum',
        'approval_status': 'ApprovalStatusEnum',
        'approval_type': 'ApprovalTypeEnum',
        'submit_time': 'datetime',
        'create_by': 'str',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'approval_time': 'datetime',
        'approver': 'str',
        'email': 'str',
        'msg': 'str',
        'directory_path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name_ch': 'name_ch',
        'name_en': 'name_en',
        'biz_id': 'biz_id',
        'biz_type': 'biz_type',
        'biz_info': 'biz_info',
        'biz_info_obj': 'biz_info_obj',
        'biz_version': 'biz_version',
        'biz_status': 'biz_status',
        'approval_status': 'approval_status',
        'approval_type': 'approval_type',
        'submit_time': 'submit_time',
        'create_by': 'create_by',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'approval_time': 'approval_time',
        'approver': 'approver',
        'email': 'email',
        'msg': 'msg',
        'directory_path': 'directory_path'
    }

    def __init__(self, id=None, tenant_id=None, name_ch=None, name_en=None, biz_id=None, biz_type=None, biz_info=None, biz_info_obj=None, biz_version=None, biz_status=None, approval_status=None, approval_type=None, submit_time=None, create_by=None, l1=None, l2=None, l3=None, approval_time=None, approver=None, email=None, msg=None, directory_path=None):
        """ApprovalVO

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: int
        :param tenant_id: tenant id
        :type tenant_id: str
        :param name_ch: 业务中文名
        :type name_ch: str
        :param name_en: 业务英文名
        :type name_en: str
        :param biz_id: 业务ID
        :type biz_id: int
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param biz_info: 业务详情
        :type biz_info: str
        :param biz_info_obj: 业务详情
        :type biz_info_obj: object
        :param biz_version: 业务版本
        :type biz_version: int
        :param biz_status: 
        :type biz_status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param approval_status: 
        :type approval_status: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalStatusEnum`
        :param approval_type: 
        :type approval_type: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalTypeEnum`
        :param submit_time: 提交时间
        :type submit_time: datetime
        :param create_by: 创建者
        :type create_by: str
        :param l1: 主题域分组
        :type l1: str
        :param l2: 主题域
        :type l2: str
        :param l3: 业务对象
        :type l3: str
        :param approval_time: 审核时间
        :type approval_time: datetime
        :param approver: 审核人
        :type approver: str
        :param email: 审核人邮箱
        :type email: str
        :param msg: 审核信息
        :type msg: str
        :param directory_path: 目录树
        :type directory_path: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name_ch = None
        self._name_en = None
        self._biz_id = None
        self._biz_type = None
        self._biz_info = None
        self._biz_info_obj = None
        self._biz_version = None
        self._biz_status = None
        self._approval_status = None
        self._approval_type = None
        self._submit_time = None
        self._create_by = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._approval_time = None
        self._approver = None
        self._email = None
        self._msg = None
        self._directory_path = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name_ch is not None:
            self.name_ch = name_ch
        if name_en is not None:
            self.name_en = name_en
        if biz_id is not None:
            self.biz_id = biz_id
        if biz_type is not None:
            self.biz_type = biz_type
        if biz_info is not None:
            self.biz_info = biz_info
        if biz_info_obj is not None:
            self.biz_info_obj = biz_info_obj
        if biz_version is not None:
            self.biz_version = biz_version
        if biz_status is not None:
            self.biz_status = biz_status
        if approval_status is not None:
            self.approval_status = approval_status
        if approval_type is not None:
            self.approval_type = approval_type
        if submit_time is not None:
            self.submit_time = submit_time
        if create_by is not None:
            self.create_by = create_by
        if l1 is not None:
            self.l1 = l1
        if l2 is not None:
            self.l2 = l2
        if l3 is not None:
            self.l3 = l3
        if approval_time is not None:
            self.approval_time = approval_time
        if approver is not None:
            self.approver = approver
        if email is not None:
            self.email = email
        if msg is not None:
            self.msg = msg
        if directory_path is not None:
            self.directory_path = directory_path

    @property
    def id(self):
        """Gets the id of this ApprovalVO.

        ID

        :return: The id of this ApprovalVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApprovalVO.

        ID

        :param id: The id of this ApprovalVO.
        :type id: int
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ApprovalVO.

        tenant id

        :return: The tenant_id of this ApprovalVO.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ApprovalVO.

        tenant id

        :param tenant_id: The tenant_id of this ApprovalVO.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name_ch(self):
        """Gets the name_ch of this ApprovalVO.

        业务中文名

        :return: The name_ch of this ApprovalVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        """Sets the name_ch of this ApprovalVO.

        业务中文名

        :param name_ch: The name_ch of this ApprovalVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def name_en(self):
        """Gets the name_en of this ApprovalVO.

        业务英文名

        :return: The name_en of this ApprovalVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this ApprovalVO.

        业务英文名

        :param name_en: The name_en of this ApprovalVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def biz_id(self):
        """Gets the biz_id of this ApprovalVO.

        业务ID

        :return: The biz_id of this ApprovalVO.
        :rtype: int
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        """Sets the biz_id of this ApprovalVO.

        业务ID

        :param biz_id: The biz_id of this ApprovalVO.
        :type biz_id: int
        """
        self._biz_id = biz_id

    @property
    def biz_type(self):
        """Gets the biz_type of this ApprovalVO.

        :return: The biz_type of this ApprovalVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this ApprovalVO.

        :param biz_type: The biz_type of this ApprovalVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def biz_info(self):
        """Gets the biz_info of this ApprovalVO.

        业务详情

        :return: The biz_info of this ApprovalVO.
        :rtype: str
        """
        return self._biz_info

    @biz_info.setter
    def biz_info(self, biz_info):
        """Sets the biz_info of this ApprovalVO.

        业务详情

        :param biz_info: The biz_info of this ApprovalVO.
        :type biz_info: str
        """
        self._biz_info = biz_info

    @property
    def biz_info_obj(self):
        """Gets the biz_info_obj of this ApprovalVO.

        业务详情

        :return: The biz_info_obj of this ApprovalVO.
        :rtype: object
        """
        return self._biz_info_obj

    @biz_info_obj.setter
    def biz_info_obj(self, biz_info_obj):
        """Sets the biz_info_obj of this ApprovalVO.

        业务详情

        :param biz_info_obj: The biz_info_obj of this ApprovalVO.
        :type biz_info_obj: object
        """
        self._biz_info_obj = biz_info_obj

    @property
    def biz_version(self):
        """Gets the biz_version of this ApprovalVO.

        业务版本

        :return: The biz_version of this ApprovalVO.
        :rtype: int
        """
        return self._biz_version

    @biz_version.setter
    def biz_version(self, biz_version):
        """Sets the biz_version of this ApprovalVO.

        业务版本

        :param biz_version: The biz_version of this ApprovalVO.
        :type biz_version: int
        """
        self._biz_version = biz_version

    @property
    def biz_status(self):
        """Gets the biz_status of this ApprovalVO.

        :return: The biz_status of this ApprovalVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._biz_status

    @biz_status.setter
    def biz_status(self, biz_status):
        """Sets the biz_status of this ApprovalVO.

        :param biz_status: The biz_status of this ApprovalVO.
        :type biz_status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._biz_status = biz_status

    @property
    def approval_status(self):
        """Gets the approval_status of this ApprovalVO.

        :return: The approval_status of this ApprovalVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalStatusEnum`
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status):
        """Sets the approval_status of this ApprovalVO.

        :param approval_status: The approval_status of this ApprovalVO.
        :type approval_status: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalStatusEnum`
        """
        self._approval_status = approval_status

    @property
    def approval_type(self):
        """Gets the approval_type of this ApprovalVO.

        :return: The approval_type of this ApprovalVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalTypeEnum`
        """
        return self._approval_type

    @approval_type.setter
    def approval_type(self, approval_type):
        """Sets the approval_type of this ApprovalVO.

        :param approval_type: The approval_type of this ApprovalVO.
        :type approval_type: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalTypeEnum`
        """
        self._approval_type = approval_type

    @property
    def submit_time(self):
        """Gets the submit_time of this ApprovalVO.

        提交时间

        :return: The submit_time of this ApprovalVO.
        :rtype: datetime
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """Sets the submit_time of this ApprovalVO.

        提交时间

        :param submit_time: The submit_time of this ApprovalVO.
        :type submit_time: datetime
        """
        self._submit_time = submit_time

    @property
    def create_by(self):
        """Gets the create_by of this ApprovalVO.

        创建者

        :return: The create_by of this ApprovalVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this ApprovalVO.

        创建者

        :param create_by: The create_by of this ApprovalVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def l1(self):
        """Gets the l1 of this ApprovalVO.

        主题域分组

        :return: The l1 of this ApprovalVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        """Sets the l1 of this ApprovalVO.

        主题域分组

        :param l1: The l1 of this ApprovalVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        """Gets the l2 of this ApprovalVO.

        主题域

        :return: The l2 of this ApprovalVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this ApprovalVO.

        主题域

        :param l2: The l2 of this ApprovalVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this ApprovalVO.

        业务对象

        :return: The l3 of this ApprovalVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this ApprovalVO.

        业务对象

        :param l3: The l3 of this ApprovalVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def approval_time(self):
        """Gets the approval_time of this ApprovalVO.

        审核时间

        :return: The approval_time of this ApprovalVO.
        :rtype: datetime
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        """Sets the approval_time of this ApprovalVO.

        审核时间

        :param approval_time: The approval_time of this ApprovalVO.
        :type approval_time: datetime
        """
        self._approval_time = approval_time

    @property
    def approver(self):
        """Gets the approver of this ApprovalVO.

        审核人

        :return: The approver of this ApprovalVO.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        """Sets the approver of this ApprovalVO.

        审核人

        :param approver: The approver of this ApprovalVO.
        :type approver: str
        """
        self._approver = approver

    @property
    def email(self):
        """Gets the email of this ApprovalVO.

        审核人邮箱

        :return: The email of this ApprovalVO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ApprovalVO.

        审核人邮箱

        :param email: The email of this ApprovalVO.
        :type email: str
        """
        self._email = email

    @property
    def msg(self):
        """Gets the msg of this ApprovalVO.

        审核信息

        :return: The msg of this ApprovalVO.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this ApprovalVO.

        审核信息

        :param msg: The msg of this ApprovalVO.
        :type msg: str
        """
        self._msg = msg

    @property
    def directory_path(self):
        """Gets the directory_path of this ApprovalVO.

        目录树

        :return: The directory_path of this ApprovalVO.
        :rtype: str
        """
        return self._directory_path

    @directory_path.setter
    def directory_path(self, directory_path):
        """Sets the directory_path of this ApprovalVO.

        目录树

        :param directory_path: The directory_path of this ApprovalVO.
        :type directory_path: str
        """
        self._directory_path = directory_path

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
        if not isinstance(other, ApprovalVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
