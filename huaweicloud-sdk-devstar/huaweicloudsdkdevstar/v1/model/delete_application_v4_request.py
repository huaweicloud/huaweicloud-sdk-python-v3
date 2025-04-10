# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteApplicationV4Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'is_delete_repository': 'bool',
        'pipeline_ids': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'is_delete_repository': 'is_delete_repository',
        'pipeline_ids': 'pipeline_ids'
    }

    def __init__(self, application_id=None, is_delete_repository=None, pipeline_ids=None):
        r"""DeleteApplicationV4Request

        The model defined in huaweicloud sdk

        :param application_id: 应用id
        :type application_id: str
        :param is_delete_repository: 是否删除代码仓
        :type is_delete_repository: bool
        :param pipeline_ids: 删除流水线ID,多流水线逗号隔开
        :type pipeline_ids: str
        """
        
        

        self._application_id = None
        self._is_delete_repository = None
        self._pipeline_ids = None
        self.discriminator = None

        self.application_id = application_id
        if is_delete_repository is not None:
            self.is_delete_repository = is_delete_repository
        if pipeline_ids is not None:
            self.pipeline_ids = pipeline_ids

    @property
    def application_id(self):
        r"""Gets the application_id of this DeleteApplicationV4Request.

        应用id

        :return: The application_id of this DeleteApplicationV4Request.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this DeleteApplicationV4Request.

        应用id

        :param application_id: The application_id of this DeleteApplicationV4Request.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def is_delete_repository(self):
        r"""Gets the is_delete_repository of this DeleteApplicationV4Request.

        是否删除代码仓

        :return: The is_delete_repository of this DeleteApplicationV4Request.
        :rtype: bool
        """
        return self._is_delete_repository

    @is_delete_repository.setter
    def is_delete_repository(self, is_delete_repository):
        r"""Sets the is_delete_repository of this DeleteApplicationV4Request.

        是否删除代码仓

        :param is_delete_repository: The is_delete_repository of this DeleteApplicationV4Request.
        :type is_delete_repository: bool
        """
        self._is_delete_repository = is_delete_repository

    @property
    def pipeline_ids(self):
        r"""Gets the pipeline_ids of this DeleteApplicationV4Request.

        删除流水线ID,多流水线逗号隔开

        :return: The pipeline_ids of this DeleteApplicationV4Request.
        :rtype: str
        """
        return self._pipeline_ids

    @pipeline_ids.setter
    def pipeline_ids(self, pipeline_ids):
        r"""Sets the pipeline_ids of this DeleteApplicationV4Request.

        删除流水线ID,多流水线逗号隔开

        :param pipeline_ids: The pipeline_ids of this DeleteApplicationV4Request.
        :type pipeline_ids: str
        """
        self._pipeline_ids = pipeline_ids

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
        if not isinstance(other, DeleteApplicationV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
