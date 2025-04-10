# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IteratorVersionsQueryInfo:

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
        'filter': 'IteratorListFilterInfo',
        'own': 'bool',
        'branch_uri': 'str',
        'iterator_uri': 'str',
        'owner_ids': 'list[str]',
        'project_uuid': 'str',
        'current_stage': 'str',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'filter': 'filter',
        'own': 'own',
        'branch_uri': 'branch_uri',
        'iterator_uri': 'iterator_uri',
        'owner_ids': 'owner_ids',
        'project_uuid': 'project_uuid',
        'current_stage': 'current_stage',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, name=None, filter=None, own=None, branch_uri=None, iterator_uri=None, owner_ids=None, project_uuid=None, current_stage=None, page_no=None, page_size=None):
        r"""IteratorVersionsQueryInfo

        The model defined in huaweicloud sdk

        :param name: 迭代计划名称（支持模糊搜索）
        :type name: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkcloudtest.v1.IteratorListFilterInfo`
        :param own: 是否是我的
        :type own: bool
        :param branch_uri: 分支URI
        :type branch_uri: str
        :param iterator_uri: 迭代计划URI
        :type iterator_uri: str
        :param owner_ids: 迭代计划责任人集合
        :type owner_ids: list[str]
        :param project_uuid: 项目ID
        :type project_uuid: str
        :param current_stage: 迭代计划所处节点
        :type current_stage: str
        :param page_no: 当前页数
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        """
        
        

        self._name = None
        self._filter = None
        self._own = None
        self._branch_uri = None
        self._iterator_uri = None
        self._owner_ids = None
        self._project_uuid = None
        self._current_stage = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if filter is not None:
            self.filter = filter
        if own is not None:
            self.own = own
        if branch_uri is not None:
            self.branch_uri = branch_uri
        if iterator_uri is not None:
            self.iterator_uri = iterator_uri
        if owner_ids is not None:
            self.owner_ids = owner_ids
        self.project_uuid = project_uuid
        if current_stage is not None:
            self.current_stage = current_stage
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def name(self):
        r"""Gets the name of this IteratorVersionsQueryInfo.

        迭代计划名称（支持模糊搜索）

        :return: The name of this IteratorVersionsQueryInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IteratorVersionsQueryInfo.

        迭代计划名称（支持模糊搜索）

        :param name: The name of this IteratorVersionsQueryInfo.
        :type name: str
        """
        self._name = name

    @property
    def filter(self):
        r"""Gets the filter of this IteratorVersionsQueryInfo.

        :return: The filter of this IteratorVersionsQueryInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.IteratorListFilterInfo`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this IteratorVersionsQueryInfo.

        :param filter: The filter of this IteratorVersionsQueryInfo.
        :type filter: :class:`huaweicloudsdkcloudtest.v1.IteratorListFilterInfo`
        """
        self._filter = filter

    @property
    def own(self):
        r"""Gets the own of this IteratorVersionsQueryInfo.

        是否是我的

        :return: The own of this IteratorVersionsQueryInfo.
        :rtype: bool
        """
        return self._own

    @own.setter
    def own(self, own):
        r"""Sets the own of this IteratorVersionsQueryInfo.

        是否是我的

        :param own: The own of this IteratorVersionsQueryInfo.
        :type own: bool
        """
        self._own = own

    @property
    def branch_uri(self):
        r"""Gets the branch_uri of this IteratorVersionsQueryInfo.

        分支URI

        :return: The branch_uri of this IteratorVersionsQueryInfo.
        :rtype: str
        """
        return self._branch_uri

    @branch_uri.setter
    def branch_uri(self, branch_uri):
        r"""Sets the branch_uri of this IteratorVersionsQueryInfo.

        分支URI

        :param branch_uri: The branch_uri of this IteratorVersionsQueryInfo.
        :type branch_uri: str
        """
        self._branch_uri = branch_uri

    @property
    def iterator_uri(self):
        r"""Gets the iterator_uri of this IteratorVersionsQueryInfo.

        迭代计划URI

        :return: The iterator_uri of this IteratorVersionsQueryInfo.
        :rtype: str
        """
        return self._iterator_uri

    @iterator_uri.setter
    def iterator_uri(self, iterator_uri):
        r"""Sets the iterator_uri of this IteratorVersionsQueryInfo.

        迭代计划URI

        :param iterator_uri: The iterator_uri of this IteratorVersionsQueryInfo.
        :type iterator_uri: str
        """
        self._iterator_uri = iterator_uri

    @property
    def owner_ids(self):
        r"""Gets the owner_ids of this IteratorVersionsQueryInfo.

        迭代计划责任人集合

        :return: The owner_ids of this IteratorVersionsQueryInfo.
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        r"""Sets the owner_ids of this IteratorVersionsQueryInfo.

        迭代计划责任人集合

        :param owner_ids: The owner_ids of this IteratorVersionsQueryInfo.
        :type owner_ids: list[str]
        """
        self._owner_ids = owner_ids

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this IteratorVersionsQueryInfo.

        项目ID

        :return: The project_uuid of this IteratorVersionsQueryInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this IteratorVersionsQueryInfo.

        项目ID

        :param project_uuid: The project_uuid of this IteratorVersionsQueryInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def current_stage(self):
        r"""Gets the current_stage of this IteratorVersionsQueryInfo.

        迭代计划所处节点

        :return: The current_stage of this IteratorVersionsQueryInfo.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        r"""Sets the current_stage of this IteratorVersionsQueryInfo.

        迭代计划所处节点

        :param current_stage: The current_stage of this IteratorVersionsQueryInfo.
        :type current_stage: str
        """
        self._current_stage = current_stage

    @property
    def page_no(self):
        r"""Gets the page_no of this IteratorVersionsQueryInfo.

        当前页数

        :return: The page_no of this IteratorVersionsQueryInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this IteratorVersionsQueryInfo.

        当前页数

        :param page_no: The page_no of this IteratorVersionsQueryInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this IteratorVersionsQueryInfo.

        每页条数

        :return: The page_size of this IteratorVersionsQueryInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this IteratorVersionsQueryInfo.

        每页条数

        :param page_size: The page_size of this IteratorVersionsQueryInfo.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, IteratorVersionsQueryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
