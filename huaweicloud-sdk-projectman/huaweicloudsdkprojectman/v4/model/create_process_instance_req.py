# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProcessInstanceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'description': 'str',
        'category': 'str',
        'need_approval': 'bool',
        'plan_end_date': 'str',
        'plan_start_date': 'str',
        'status': 'str',
        'cc': 'list[str]',
        'attach_wikis': 'list[str]',
        'attach_documents': 'list[str]',
        'ccbs': 'list[CreateProcessInstanceReqCcbs]',
        'opinions': 'list[CreateProcessInstanceReqOpinions]',
        'cos': 'list[CreateProcessInstanceReqCos]',
        'local_attachment_names': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'category': 'category',
        'need_approval': 'need_approval',
        'plan_end_date': 'plan_end_date',
        'plan_start_date': 'plan_start_date',
        'status': 'status',
        'cc': 'cc',
        'attach_wikis': 'attachWikis',
        'attach_documents': 'attachDocuments',
        'ccbs': 'ccbs',
        'opinions': 'opinions',
        'cos': 'cos',
        'local_attachment_names': 'local_attachment_names'
    }

    def __init__(self, title=None, description=None, category=None, need_approval=None, plan_end_date=None, plan_start_date=None, status=None, cc=None, attach_wikis=None, attach_documents=None, ccbs=None, opinions=None, cos=None, local_attachment_names=None):
        r"""CreateProcessInstanceReq

        The model defined in huaweicloud sdk

        :param title: 标题
        :type title: str
        :param description: 描述
        :type description: str
        :param category: 类别
        :type category: str
        :param need_approval: 是否需要决策人审批
        :type need_approval: bool
        :param plan_end_date: 计划完成日期时间戳，不可早于计划开始日期
        :type plan_end_date: str
        :param plan_start_date: 计划开始日期时间戳，不可晚于计划完成日期
        :type plan_start_date: str
        :param status: 状态
        :type status: str
        :param cc: 抄送人列表
        :type cc: list[str]
        :param attach_wikis: 关联wiki
        :type attach_wikis: list[str]
        :param attach_documents: 关联文件
        :type attach_documents: list[str]
        :param ccbs: 决策人
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReqCcbs`]
        :param opinions: 评审专家
        :type opinions: list[:class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReqOpinions`]
        :param cos: 评审对象
        :type cos: list[:class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReqCos`]
        :param local_attachment_names: 关联文件名
        :type local_attachment_names: list[str]
        """
        
        

        self._title = None
        self._description = None
        self._category = None
        self._need_approval = None
        self._plan_end_date = None
        self._plan_start_date = None
        self._status = None
        self._cc = None
        self._attach_wikis = None
        self._attach_documents = None
        self._ccbs = None
        self._opinions = None
        self._cos = None
        self._local_attachment_names = None
        self.discriminator = None

        self.title = title
        self.description = description
        self.category = category
        if need_approval is not None:
            self.need_approval = need_approval
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        self.status = status
        if cc is not None:
            self.cc = cc
        if attach_wikis is not None:
            self.attach_wikis = attach_wikis
        if attach_documents is not None:
            self.attach_documents = attach_documents
        if ccbs is not None:
            self.ccbs = ccbs
        if opinions is not None:
            self.opinions = opinions
        if cos is not None:
            self.cos = cos
        if local_attachment_names is not None:
            self.local_attachment_names = local_attachment_names

    @property
    def title(self):
        r"""Gets the title of this CreateProcessInstanceReq.

        标题

        :return: The title of this CreateProcessInstanceReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateProcessInstanceReq.

        标题

        :param title: The title of this CreateProcessInstanceReq.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this CreateProcessInstanceReq.

        描述

        :return: The description of this CreateProcessInstanceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateProcessInstanceReq.

        描述

        :param description: The description of this CreateProcessInstanceReq.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        r"""Gets the category of this CreateProcessInstanceReq.

        类别

        :return: The category of this CreateProcessInstanceReq.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateProcessInstanceReq.

        类别

        :param category: The category of this CreateProcessInstanceReq.
        :type category: str
        """
        self._category = category

    @property
    def need_approval(self):
        r"""Gets the need_approval of this CreateProcessInstanceReq.

        是否需要决策人审批

        :return: The need_approval of this CreateProcessInstanceReq.
        :rtype: bool
        """
        return self._need_approval

    @need_approval.setter
    def need_approval(self, need_approval):
        r"""Sets the need_approval of this CreateProcessInstanceReq.

        是否需要决策人审批

        :param need_approval: The need_approval of this CreateProcessInstanceReq.
        :type need_approval: bool
        """
        self._need_approval = need_approval

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this CreateProcessInstanceReq.

        计划完成日期时间戳，不可早于计划开始日期

        :return: The plan_end_date of this CreateProcessInstanceReq.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this CreateProcessInstanceReq.

        计划完成日期时间戳，不可早于计划开始日期

        :param plan_end_date: The plan_end_date of this CreateProcessInstanceReq.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def plan_start_date(self):
        r"""Gets the plan_start_date of this CreateProcessInstanceReq.

        计划开始日期时间戳，不可晚于计划完成日期

        :return: The plan_start_date of this CreateProcessInstanceReq.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        r"""Sets the plan_start_date of this CreateProcessInstanceReq.

        计划开始日期时间戳，不可晚于计划完成日期

        :param plan_start_date: The plan_start_date of this CreateProcessInstanceReq.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def status(self):
        r"""Gets the status of this CreateProcessInstanceReq.

        状态

        :return: The status of this CreateProcessInstanceReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateProcessInstanceReq.

        状态

        :param status: The status of this CreateProcessInstanceReq.
        :type status: str
        """
        self._status = status

    @property
    def cc(self):
        r"""Gets the cc of this CreateProcessInstanceReq.

        抄送人列表

        :return: The cc of this CreateProcessInstanceReq.
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this CreateProcessInstanceReq.

        抄送人列表

        :param cc: The cc of this CreateProcessInstanceReq.
        :type cc: list[str]
        """
        self._cc = cc

    @property
    def attach_wikis(self):
        r"""Gets the attach_wikis of this CreateProcessInstanceReq.

        关联wiki

        :return: The attach_wikis of this CreateProcessInstanceReq.
        :rtype: list[str]
        """
        return self._attach_wikis

    @attach_wikis.setter
    def attach_wikis(self, attach_wikis):
        r"""Sets the attach_wikis of this CreateProcessInstanceReq.

        关联wiki

        :param attach_wikis: The attach_wikis of this CreateProcessInstanceReq.
        :type attach_wikis: list[str]
        """
        self._attach_wikis = attach_wikis

    @property
    def attach_documents(self):
        r"""Gets the attach_documents of this CreateProcessInstanceReq.

        关联文件

        :return: The attach_documents of this CreateProcessInstanceReq.
        :rtype: list[str]
        """
        return self._attach_documents

    @attach_documents.setter
    def attach_documents(self, attach_documents):
        r"""Sets the attach_documents of this CreateProcessInstanceReq.

        关联文件

        :param attach_documents: The attach_documents of this CreateProcessInstanceReq.
        :type attach_documents: list[str]
        """
        self._attach_documents = attach_documents

    @property
    def ccbs(self):
        r"""Gets the ccbs of this CreateProcessInstanceReq.

        决策人

        :return: The ccbs of this CreateProcessInstanceReq.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReqCcbs`]
        """
        return self._ccbs

    @ccbs.setter
    def ccbs(self, ccbs):
        r"""Sets the ccbs of this CreateProcessInstanceReq.

        决策人

        :param ccbs: The ccbs of this CreateProcessInstanceReq.
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReqCcbs`]
        """
        self._ccbs = ccbs

    @property
    def opinions(self):
        r"""Gets the opinions of this CreateProcessInstanceReq.

        评审专家

        :return: The opinions of this CreateProcessInstanceReq.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReqOpinions`]
        """
        return self._opinions

    @opinions.setter
    def opinions(self, opinions):
        r"""Sets the opinions of this CreateProcessInstanceReq.

        评审专家

        :param opinions: The opinions of this CreateProcessInstanceReq.
        :type opinions: list[:class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReqOpinions`]
        """
        self._opinions = opinions

    @property
    def cos(self):
        r"""Gets the cos of this CreateProcessInstanceReq.

        评审对象

        :return: The cos of this CreateProcessInstanceReq.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReqCos`]
        """
        return self._cos

    @cos.setter
    def cos(self, cos):
        r"""Sets the cos of this CreateProcessInstanceReq.

        评审对象

        :param cos: The cos of this CreateProcessInstanceReq.
        :type cos: list[:class:`huaweicloudsdkprojectman.v4.CreateProcessInstanceReqCos`]
        """
        self._cos = cos

    @property
    def local_attachment_names(self):
        r"""Gets the local_attachment_names of this CreateProcessInstanceReq.

        关联文件名

        :return: The local_attachment_names of this CreateProcessInstanceReq.
        :rtype: list[str]
        """
        return self._local_attachment_names

    @local_attachment_names.setter
    def local_attachment_names(self, local_attachment_names):
        r"""Sets the local_attachment_names of this CreateProcessInstanceReq.

        关联文件名

        :param local_attachment_names: The local_attachment_names of this CreateProcessInstanceReq.
        :type local_attachment_names: list[str]
        """
        self._local_attachment_names = local_attachment_names

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
        if not isinstance(other, CreateProcessInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
