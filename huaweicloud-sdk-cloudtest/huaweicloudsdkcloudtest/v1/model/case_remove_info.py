# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseRemoveInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'iterator_uri': 'str',
        'remove_associate_issue': 'bool',
        'case_list': 'list[CaseIdAndTypeInfo]'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'iterator_uri': 'iterator_uri',
        'remove_associate_issue': 'remove_associate_issue',
        'case_list': 'case_list'
    }

    def __init__(self, project_uuid=None, iterator_uri=None, remove_associate_issue=None, case_list=None):
        """CaseRemoveInfo

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param iterator_uri: 迭代Uri
        :type iterator_uri: str
        :param remove_associate_issue: 是否移除关联的issue
        :type remove_associate_issue: bool
        :param case_list: 用例列表信息
        :type case_list: list[:class:`huaweicloudsdkcloudtest.v1.CaseIdAndTypeInfo`]
        """
        
        

        self._project_uuid = None
        self._iterator_uri = None
        self._remove_associate_issue = None
        self._case_list = None
        self.discriminator = None

        if project_uuid is not None:
            self.project_uuid = project_uuid
        if iterator_uri is not None:
            self.iterator_uri = iterator_uri
        if remove_associate_issue is not None:
            self.remove_associate_issue = remove_associate_issue
        if case_list is not None:
            self.case_list = case_list

    @property
    def project_uuid(self):
        """Gets the project_uuid of this CaseRemoveInfo.

        项目id

        :return: The project_uuid of this CaseRemoveInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this CaseRemoveInfo.

        项目id

        :param project_uuid: The project_uuid of this CaseRemoveInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def iterator_uri(self):
        """Gets the iterator_uri of this CaseRemoveInfo.

        迭代Uri

        :return: The iterator_uri of this CaseRemoveInfo.
        :rtype: str
        """
        return self._iterator_uri

    @iterator_uri.setter
    def iterator_uri(self, iterator_uri):
        """Sets the iterator_uri of this CaseRemoveInfo.

        迭代Uri

        :param iterator_uri: The iterator_uri of this CaseRemoveInfo.
        :type iterator_uri: str
        """
        self._iterator_uri = iterator_uri

    @property
    def remove_associate_issue(self):
        """Gets the remove_associate_issue of this CaseRemoveInfo.

        是否移除关联的issue

        :return: The remove_associate_issue of this CaseRemoveInfo.
        :rtype: bool
        """
        return self._remove_associate_issue

    @remove_associate_issue.setter
    def remove_associate_issue(self, remove_associate_issue):
        """Sets the remove_associate_issue of this CaseRemoveInfo.

        是否移除关联的issue

        :param remove_associate_issue: The remove_associate_issue of this CaseRemoveInfo.
        :type remove_associate_issue: bool
        """
        self._remove_associate_issue = remove_associate_issue

    @property
    def case_list(self):
        """Gets the case_list of this CaseRemoveInfo.

        用例列表信息

        :return: The case_list of this CaseRemoveInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CaseIdAndTypeInfo`]
        """
        return self._case_list

    @case_list.setter
    def case_list(self, case_list):
        """Sets the case_list of this CaseRemoveInfo.

        用例列表信息

        :param case_list: The case_list of this CaseRemoveInfo.
        :type case_list: list[:class:`huaweicloudsdkcloudtest.v1.CaseIdAndTypeInfo`]
        """
        self._case_list = case_list

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
        if not isinstance(other, CaseRemoveInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
