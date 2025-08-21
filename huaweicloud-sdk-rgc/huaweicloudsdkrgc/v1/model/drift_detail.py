# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DriftDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_account_id': 'str',
        'drift_type': 'str',
        'drift_target_id': 'str',
        'drift_target_type': 'str',
        'drift_message': 'str',
        'parent_organizational_unit_id': 'str',
        'solve_solution': 'str'
    }

    attribute_map = {
        'managed_account_id': 'managed_account_id',
        'drift_type': 'drift_type',
        'drift_target_id': 'drift_target_id',
        'drift_target_type': 'drift_target_type',
        'drift_message': 'drift_message',
        'parent_organizational_unit_id': 'parent_organizational_unit_id',
        'solve_solution': 'solve_solution'
    }

    def __init__(self, managed_account_id=None, drift_type=None, drift_target_id=None, drift_target_type=None, drift_message=None, parent_organizational_unit_id=None, solve_solution=None):
        r"""DriftDetail

        The model defined in huaweicloud sdk

        :param managed_account_id: 管理员账号ID。
        :type managed_account_id: str
        :param drift_type: 漂移类型。
        :type drift_type: str
        :param drift_target_id: 漂移发生的纳管账号ID或注册OU ID。
        :type drift_target_id: str
        :param drift_target_type: 漂移目标类型，类型有account、ou和policy。
        :type drift_target_type: str
        :param drift_message: 漂移信息。
        :type drift_message: str
        :param parent_organizational_unit_id: 父注册OU ID。
        :type parent_organizational_unit_id: str
        :param solve_solution: 漂移修复方法。
        :type solve_solution: str
        """
        
        

        self._managed_account_id = None
        self._drift_type = None
        self._drift_target_id = None
        self._drift_target_type = None
        self._drift_message = None
        self._parent_organizational_unit_id = None
        self._solve_solution = None
        self.discriminator = None

        if managed_account_id is not None:
            self.managed_account_id = managed_account_id
        if drift_type is not None:
            self.drift_type = drift_type
        if drift_target_id is not None:
            self.drift_target_id = drift_target_id
        if drift_target_type is not None:
            self.drift_target_type = drift_target_type
        if drift_message is not None:
            self.drift_message = drift_message
        if parent_organizational_unit_id is not None:
            self.parent_organizational_unit_id = parent_organizational_unit_id
        if solve_solution is not None:
            self.solve_solution = solve_solution

    @property
    def managed_account_id(self):
        r"""Gets the managed_account_id of this DriftDetail.

        管理员账号ID。

        :return: The managed_account_id of this DriftDetail.
        :rtype: str
        """
        return self._managed_account_id

    @managed_account_id.setter
    def managed_account_id(self, managed_account_id):
        r"""Sets the managed_account_id of this DriftDetail.

        管理员账号ID。

        :param managed_account_id: The managed_account_id of this DriftDetail.
        :type managed_account_id: str
        """
        self._managed_account_id = managed_account_id

    @property
    def drift_type(self):
        r"""Gets the drift_type of this DriftDetail.

        漂移类型。

        :return: The drift_type of this DriftDetail.
        :rtype: str
        """
        return self._drift_type

    @drift_type.setter
    def drift_type(self, drift_type):
        r"""Sets the drift_type of this DriftDetail.

        漂移类型。

        :param drift_type: The drift_type of this DriftDetail.
        :type drift_type: str
        """
        self._drift_type = drift_type

    @property
    def drift_target_id(self):
        r"""Gets the drift_target_id of this DriftDetail.

        漂移发生的纳管账号ID或注册OU ID。

        :return: The drift_target_id of this DriftDetail.
        :rtype: str
        """
        return self._drift_target_id

    @drift_target_id.setter
    def drift_target_id(self, drift_target_id):
        r"""Sets the drift_target_id of this DriftDetail.

        漂移发生的纳管账号ID或注册OU ID。

        :param drift_target_id: The drift_target_id of this DriftDetail.
        :type drift_target_id: str
        """
        self._drift_target_id = drift_target_id

    @property
    def drift_target_type(self):
        r"""Gets the drift_target_type of this DriftDetail.

        漂移目标类型，类型有account、ou和policy。

        :return: The drift_target_type of this DriftDetail.
        :rtype: str
        """
        return self._drift_target_type

    @drift_target_type.setter
    def drift_target_type(self, drift_target_type):
        r"""Sets the drift_target_type of this DriftDetail.

        漂移目标类型，类型有account、ou和policy。

        :param drift_target_type: The drift_target_type of this DriftDetail.
        :type drift_target_type: str
        """
        self._drift_target_type = drift_target_type

    @property
    def drift_message(self):
        r"""Gets the drift_message of this DriftDetail.

        漂移信息。

        :return: The drift_message of this DriftDetail.
        :rtype: str
        """
        return self._drift_message

    @drift_message.setter
    def drift_message(self, drift_message):
        r"""Sets the drift_message of this DriftDetail.

        漂移信息。

        :param drift_message: The drift_message of this DriftDetail.
        :type drift_message: str
        """
        self._drift_message = drift_message

    @property
    def parent_organizational_unit_id(self):
        r"""Gets the parent_organizational_unit_id of this DriftDetail.

        父注册OU ID。

        :return: The parent_organizational_unit_id of this DriftDetail.
        :rtype: str
        """
        return self._parent_organizational_unit_id

    @parent_organizational_unit_id.setter
    def parent_organizational_unit_id(self, parent_organizational_unit_id):
        r"""Sets the parent_organizational_unit_id of this DriftDetail.

        父注册OU ID。

        :param parent_organizational_unit_id: The parent_organizational_unit_id of this DriftDetail.
        :type parent_organizational_unit_id: str
        """
        self._parent_organizational_unit_id = parent_organizational_unit_id

    @property
    def solve_solution(self):
        r"""Gets the solve_solution of this DriftDetail.

        漂移修复方法。

        :return: The solve_solution of this DriftDetail.
        :rtype: str
        """
        return self._solve_solution

    @solve_solution.setter
    def solve_solution(self, solve_solution):
        r"""Sets the solve_solution of this DriftDetail.

        漂移修复方法。

        :param solve_solution: The solve_solution of this DriftDetail.
        :type solve_solution: str
        """
        self._solve_solution = solve_solution

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
        if not isinstance(other, DriftDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
