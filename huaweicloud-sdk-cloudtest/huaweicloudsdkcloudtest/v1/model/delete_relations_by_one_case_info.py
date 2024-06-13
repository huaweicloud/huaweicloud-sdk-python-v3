# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRelationsByOneCaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_item_ids': 'list[str]',
        'project_uuid': 'str',
        'version_uri': 'str',
        'relate_type': 'str'
    }

    attribute_map = {
        'work_item_ids': 'work_item_ids',
        'project_uuid': 'project_uuid',
        'version_uri': 'version_uri',
        'relate_type': 'relate_type'
    }

    def __init__(self, work_item_ids=None, project_uuid=None, version_uri=None, relate_type=None):
        """DeleteRelationsByOneCaseInfo

        The model defined in huaweicloud sdk

        :param work_item_ids: 
        :type work_item_ids: list[str]
        :param project_uuid: 项目id
        :type project_uuid: str
        :param version_uri: 版本uri
        :type version_uri: str
        :param relate_type: 关联关系类型
        :type relate_type: str
        """
        
        

        self._work_item_ids = None
        self._project_uuid = None
        self._version_uri = None
        self._relate_type = None
        self.discriminator = None

        if work_item_ids is not None:
            self.work_item_ids = work_item_ids
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if version_uri is not None:
            self.version_uri = version_uri
        if relate_type is not None:
            self.relate_type = relate_type

    @property
    def work_item_ids(self):
        """Gets the work_item_ids of this DeleteRelationsByOneCaseInfo.

        :return: The work_item_ids of this DeleteRelationsByOneCaseInfo.
        :rtype: list[str]
        """
        return self._work_item_ids

    @work_item_ids.setter
    def work_item_ids(self, work_item_ids):
        """Sets the work_item_ids of this DeleteRelationsByOneCaseInfo.

        :param work_item_ids: The work_item_ids of this DeleteRelationsByOneCaseInfo.
        :type work_item_ids: list[str]
        """
        self._work_item_ids = work_item_ids

    @property
    def project_uuid(self):
        """Gets the project_uuid of this DeleteRelationsByOneCaseInfo.

        项目id

        :return: The project_uuid of this DeleteRelationsByOneCaseInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this DeleteRelationsByOneCaseInfo.

        项目id

        :param project_uuid: The project_uuid of this DeleteRelationsByOneCaseInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def version_uri(self):
        """Gets the version_uri of this DeleteRelationsByOneCaseInfo.

        版本uri

        :return: The version_uri of this DeleteRelationsByOneCaseInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this DeleteRelationsByOneCaseInfo.

        版本uri

        :param version_uri: The version_uri of this DeleteRelationsByOneCaseInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def relate_type(self):
        """Gets the relate_type of this DeleteRelationsByOneCaseInfo.

        关联关系类型

        :return: The relate_type of this DeleteRelationsByOneCaseInfo.
        :rtype: str
        """
        return self._relate_type

    @relate_type.setter
    def relate_type(self, relate_type):
        """Sets the relate_type of this DeleteRelationsByOneCaseInfo.

        关联关系类型

        :param relate_type: The relate_type of this DeleteRelationsByOneCaseInfo.
        :type relate_type: str
        """
        self._relate_type = relate_type

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
        if not isinstance(other, DeleteRelationsByOneCaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
