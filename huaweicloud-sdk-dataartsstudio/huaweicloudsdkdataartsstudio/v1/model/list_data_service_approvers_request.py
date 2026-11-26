# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataServiceApproversRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'page': 'int',
        'size': 'int',
        'approver_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'page': 'page',
        'size': 'size',
        'approver_name': 'approver_name'
    }

    def __init__(self, workspace=None, dlm_type=None, page=None, size=None, approver_name=None):
        r"""ListDataServiceApproversRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param dlm_type: 数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。
        :type dlm_type: str
        :param page: 页码
        :type page: int
        :param size: 每页记录数
        :type size: int
        :param approver_name: 审批人名字
        :type approver_name: str
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._page = None
        self._size = None
        self._approver_name = None
        self.discriminator = None

        self.workspace = workspace
        if dlm_type is not None:
            self.dlm_type = dlm_type
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if approver_name is not None:
            self.approver_name = approver_name

    @property
    def workspace(self):
        r"""Gets the workspace of this ListDataServiceApproversRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListDataServiceApproversRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListDataServiceApproversRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListDataServiceApproversRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        r"""Gets the dlm_type of this ListDataServiceApproversRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this ListDataServiceApproversRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        r"""Sets the dlm_type of this ListDataServiceApproversRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this ListDataServiceApproversRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def page(self):
        r"""Gets the page of this ListDataServiceApproversRequest.

        页码

        :return: The page of this ListDataServiceApproversRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListDataServiceApproversRequest.

        页码

        :param page: The page of this ListDataServiceApproversRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this ListDataServiceApproversRequest.

        每页记录数

        :return: The size of this ListDataServiceApproversRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListDataServiceApproversRequest.

        每页记录数

        :param size: The size of this ListDataServiceApproversRequest.
        :type size: int
        """
        self._size = size

    @property
    def approver_name(self):
        r"""Gets the approver_name of this ListDataServiceApproversRequest.

        审批人名字

        :return: The approver_name of this ListDataServiceApproversRequest.
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        r"""Sets the approver_name of this ListDataServiceApproversRequest.

        审批人名字

        :param approver_name: The approver_name of this ListDataServiceApproversRequest.
        :type approver_name: str
        """
        self._approver_name = approver_name

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
        if not isinstance(other, ListDataServiceApproversRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
