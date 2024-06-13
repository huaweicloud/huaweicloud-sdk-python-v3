# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequirementOverviewVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'workitem_id': 'str',
        'sequence_id': 'str',
        'board_id': 'str',
        'tracker_id': 'str',
        'tracker_name': 'str',
        'relate_case_number': 'int',
        'case_pass_vo': 'CasePassVo',
        'case_execute_vo': 'CaseExecuteVo',
        'relate_defect_number': 'int'
    }

    attribute_map = {
        'name': 'name',
        'workitem_id': 'workitem_id',
        'sequence_id': 'sequence_id',
        'board_id': 'board_id',
        'tracker_id': 'tracker_id',
        'tracker_name': 'tracker_name',
        'relate_case_number': 'relate_case_number',
        'case_pass_vo': 'case_pass_vo',
        'case_execute_vo': 'case_execute_vo',
        'relate_defect_number': 'relate_defect_number'
    }

    def __init__(self, name=None, workitem_id=None, sequence_id=None, board_id=None, tracker_id=None, tracker_name=None, relate_case_number=None, case_pass_vo=None, case_execute_vo=None, relate_defect_number=None):
        """RequirementOverviewVo

        The model defined in huaweicloud sdk

        :param name: 需求名称
        :type name: str
        :param workitem_id: 需求id
        :type workitem_id: str
        :param sequence_id: 需求序列编号
        :type sequence_id: str
        :param board_id: 看板需求id
        :type board_id: str
        :param tracker_id: 需求类型id
        :type tracker_id: str
        :param tracker_name: 需求类型
        :type tracker_name: str
        :param relate_case_number: 需求关联用例总数
        :type relate_case_number: int
        :param case_pass_vo: 
        :type case_pass_vo: :class:`huaweicloudsdkcloudtest.v1.CasePassVo`
        :param case_execute_vo: 
        :type case_execute_vo: :class:`huaweicloudsdkcloudtest.v1.CaseExecuteVo`
        :param relate_defect_number: 需求关联缺陷总数
        :type relate_defect_number: int
        """
        
        

        self._name = None
        self._workitem_id = None
        self._sequence_id = None
        self._board_id = None
        self._tracker_id = None
        self._tracker_name = None
        self._relate_case_number = None
        self._case_pass_vo = None
        self._case_execute_vo = None
        self._relate_defect_number = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if workitem_id is not None:
            self.workitem_id = workitem_id
        if sequence_id is not None:
            self.sequence_id = sequence_id
        if board_id is not None:
            self.board_id = board_id
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if tracker_name is not None:
            self.tracker_name = tracker_name
        if relate_case_number is not None:
            self.relate_case_number = relate_case_number
        if case_pass_vo is not None:
            self.case_pass_vo = case_pass_vo
        if case_execute_vo is not None:
            self.case_execute_vo = case_execute_vo
        if relate_defect_number is not None:
            self.relate_defect_number = relate_defect_number

    @property
    def name(self):
        """Gets the name of this RequirementOverviewVo.

        需求名称

        :return: The name of this RequirementOverviewVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RequirementOverviewVo.

        需求名称

        :param name: The name of this RequirementOverviewVo.
        :type name: str
        """
        self._name = name

    @property
    def workitem_id(self):
        """Gets the workitem_id of this RequirementOverviewVo.

        需求id

        :return: The workitem_id of this RequirementOverviewVo.
        :rtype: str
        """
        return self._workitem_id

    @workitem_id.setter
    def workitem_id(self, workitem_id):
        """Sets the workitem_id of this RequirementOverviewVo.

        需求id

        :param workitem_id: The workitem_id of this RequirementOverviewVo.
        :type workitem_id: str
        """
        self._workitem_id = workitem_id

    @property
    def sequence_id(self):
        """Gets the sequence_id of this RequirementOverviewVo.

        需求序列编号

        :return: The sequence_id of this RequirementOverviewVo.
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """Sets the sequence_id of this RequirementOverviewVo.

        需求序列编号

        :param sequence_id: The sequence_id of this RequirementOverviewVo.
        :type sequence_id: str
        """
        self._sequence_id = sequence_id

    @property
    def board_id(self):
        """Gets the board_id of this RequirementOverviewVo.

        看板需求id

        :return: The board_id of this RequirementOverviewVo.
        :rtype: str
        """
        return self._board_id

    @board_id.setter
    def board_id(self, board_id):
        """Sets the board_id of this RequirementOverviewVo.

        看板需求id

        :param board_id: The board_id of this RequirementOverviewVo.
        :type board_id: str
        """
        self._board_id = board_id

    @property
    def tracker_id(self):
        """Gets the tracker_id of this RequirementOverviewVo.

        需求类型id

        :return: The tracker_id of this RequirementOverviewVo.
        :rtype: str
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        """Sets the tracker_id of this RequirementOverviewVo.

        需求类型id

        :param tracker_id: The tracker_id of this RequirementOverviewVo.
        :type tracker_id: str
        """
        self._tracker_id = tracker_id

    @property
    def tracker_name(self):
        """Gets the tracker_name of this RequirementOverviewVo.

        需求类型

        :return: The tracker_name of this RequirementOverviewVo.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this RequirementOverviewVo.

        需求类型

        :param tracker_name: The tracker_name of this RequirementOverviewVo.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

    @property
    def relate_case_number(self):
        """Gets the relate_case_number of this RequirementOverviewVo.

        需求关联用例总数

        :return: The relate_case_number of this RequirementOverviewVo.
        :rtype: int
        """
        return self._relate_case_number

    @relate_case_number.setter
    def relate_case_number(self, relate_case_number):
        """Sets the relate_case_number of this RequirementOverviewVo.

        需求关联用例总数

        :param relate_case_number: The relate_case_number of this RequirementOverviewVo.
        :type relate_case_number: int
        """
        self._relate_case_number = relate_case_number

    @property
    def case_pass_vo(self):
        """Gets the case_pass_vo of this RequirementOverviewVo.

        :return: The case_pass_vo of this RequirementOverviewVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CasePassVo`
        """
        return self._case_pass_vo

    @case_pass_vo.setter
    def case_pass_vo(self, case_pass_vo):
        """Sets the case_pass_vo of this RequirementOverviewVo.

        :param case_pass_vo: The case_pass_vo of this RequirementOverviewVo.
        :type case_pass_vo: :class:`huaweicloudsdkcloudtest.v1.CasePassVo`
        """
        self._case_pass_vo = case_pass_vo

    @property
    def case_execute_vo(self):
        """Gets the case_execute_vo of this RequirementOverviewVo.

        :return: The case_execute_vo of this RequirementOverviewVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CaseExecuteVo`
        """
        return self._case_execute_vo

    @case_execute_vo.setter
    def case_execute_vo(self, case_execute_vo):
        """Sets the case_execute_vo of this RequirementOverviewVo.

        :param case_execute_vo: The case_execute_vo of this RequirementOverviewVo.
        :type case_execute_vo: :class:`huaweicloudsdkcloudtest.v1.CaseExecuteVo`
        """
        self._case_execute_vo = case_execute_vo

    @property
    def relate_defect_number(self):
        """Gets the relate_defect_number of this RequirementOverviewVo.

        需求关联缺陷总数

        :return: The relate_defect_number of this RequirementOverviewVo.
        :rtype: int
        """
        return self._relate_defect_number

    @relate_defect_number.setter
    def relate_defect_number(self, relate_defect_number):
        """Sets the relate_defect_number of this RequirementOverviewVo.

        需求关联缺陷总数

        :param relate_defect_number: The relate_defect_number of this RequirementOverviewVo.
        :type relate_defect_number: int
        """
        self._relate_defect_number = relate_defect_number

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
        if not isinstance(other, RequirementOverviewVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
